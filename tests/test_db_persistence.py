
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from eo_lib.domain.base import Base
from eo_lib.domain.entities import Team, Person, Organization, OrganizationalUnit
from research_domain.domain.entities.research_group import ResearchGroup
from research_domain.domain.entities.researcher import Researcher
from libbase.infrastructure.sql_repository import GenericSqlRepository

# Create an in-memory SQLite engine
engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(bind=engine)

def setup_module(module):
    """
    Create tables in the in-memory database.
    """
    Base.metadata.create_all(bind=engine)

def test_research_group_persistence_and_retrieval():
    """
    Test saving a ResearchGroup to DB and retrieving it.
    Verifies that 'to_dict' works correctly on the retrieved SQLAlchemy object
    and contains both Parent (Team) and Child (ResearchGroup) data.
    """
    session = SessionLocal()
    
    # 1. Setup minimal dependency (Organization -> Campus)
    # Organization
    org = Organization(name="Test Org")
    session.add(org)
    session.commit()
    
    # Campus (OrganizationalUnit)
    campus = OrganizationalUnit(name="Test Campus", organization_id=org.id)
    session.add(campus)
    session.commit()
    campus_id = campus.id
    
    # 2. Create ResearchGroup
    group = ResearchGroup(
        name="Persisted Group",          # Parent
        description="Stored in DB",      # Parent
        campus_id=campus_id,             # Child
        cnpq_url="http://db.cnpq.br"     # Child
    )
    
    # 3. Persist
    repo = GenericSqlRepository(session, ResearchGroup)
    repo.add(group)
    session.commit()
    group_id = group.id
    
    # 4. Clear session to force reload from DB
    session.close()
    session = SessionLocal()
    
    # 5. Retrieve
    print("DEBUG: Using direct session query with NEW session...")
    try:
        # retrieved_group = repo.get_by_id(group.id)
        retrieved_group = session.query(ResearchGroup).filter_by(id=group_id).first()
        
        # print(f"DEBUG: Query returned {retrieved_group}")  # Causes DetachedInstanceError if __repr__ hits lazy fields
        print(f"DEBUG: Session is active? {session.is_active}")
        print(f"DEBUG: Object attached? {retrieved_group in session}")
    except Exception as e:
        print(f"DEBUG: Error during query: {e}")
        raise e
    
    assert retrieved_group is not None
    
    # 6. Verify Data Access via Attributes
    print("DEBUG: Accessing attributes...")
    try:
        n = retrieved_group.name  # Should trigger loading if lazy
        print(f"DEBUG: Accessed name: {n}")
        d = retrieved_group.description
        print(f"DEBUG: Accessed description: {d}")
        c = retrieved_group.campus_id
        print(f"DEBUG: Accessed campus_id: {c}")
    except Exception as e:
        print(f"DEBUG: Error accessing attributes: {e}")
        raise e
    
    assert retrieved_group.name == "Persisted Group"
    assert retrieved_group.description == "Stored in DB"
    assert retrieved_group.campus_id == campus_id
    
    # 7. Verify Data Serialization (The fix)
    print("DEBUG: Calling to_dict...")
    data = retrieved_group.to_dict()
    print("DEBUG: to_dict succeeded")

    
    # Check Parent Data in Dict
    assert "name" in data
    assert data["name"] == "Persisted Group"
    
    # Check Child Data in Dict
    assert "cnpq_url" in data
    assert data["cnpq_url"] == "http://db.cnpq.br"
    
    session.close()

def test_researcher_persistence_and_retrieval():
    """
    Test saving a Researcher to DB and retrieving it.
    """
    session = SessionLocal()
    
    # 1. Create Researcher
    researcher = Researcher(
        name="Persisted Researcher",
        cnpq_url="http://lattes.br/p"
    )
    
    # 2. Persist
    repo = GenericSqlRepository(session, Researcher)
    repo.add(researcher)
    session.commit()
    researcher_id = researcher.id
    
    # 3. Clear session
    session.close()
    session = SessionLocal()
    
    # 4. Retrieve
    retrieved = session.query(Researcher).filter_by(id=researcher_id).first()
    
    # 5. Verify Serialization
    data = retrieved.to_dict()
    
    assert data["name"] == "Persisted Researcher"
    assert data["cnpq_url"] == "http://lattes.br/p"
    
    session.close()
