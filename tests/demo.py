import os
from sqlalchemy import text
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from eo_lib.domain.base import Base

# Try to load .env for local configuration
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import all research domain entities
from research_domain import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    KnowledgeArea,
    ResearcherController,
    UniversityController,
    CampusController,
    ResearchGroupController,
    KnowledgeAreaController,
    RoleController,
)

# Also import eo_lib entities
from eo_lib.domain.entities import (
    Person,
    PersonEmail,
    Team,
    TeamMember,
    Role,
    Organization,
    OrganizationalUnit,
)

def setup_database():
    """Initializes the database by dropping and recreating all tables."""
    storage_type = os.getenv("STORAGE_TYPE", "memory").lower()
    if storage_type not in ["postgres", "db"]:
        print(f"Skipping database initialization (STORAGE_TYPE is '{storage_type}').")
        return

    print("Initializing Database Tables...")
    client = PostgresClient()
    
    # Force drop all tables via CASCADE to handle constraints
    try:
        with client._engine.connect() as conn:
            print("Performing forced cleanup (DROP SCHEMA public CASCADE)...")
            conn.execute(text("DROP SCHEMA public CASCADE"))
            conn.execute(text("CREATE SCHEMA public"))
            conn.execute(text("GRANT ALL ON SCHEMA public TO public"))
            conn.execute(text("GRANT ALL ON SCHEMA public TO postgres"))
            conn.commit()
    except Exception as e:
        print(f"Note: Error during forced cleanup (ignored): {e}")

    print("Recreating all tables via Base.metadata...")
    Base.metadata.create_all(client._engine)
    print("Database tables initialized successfully.")

def run_demo():
    print("--- Starting ResearchDomain Advanced Demo ---")
    setup_database()
    
    try:
        # 1. Initialize Controllers
        uni_ctrl = UniversityController()
        campus_ctrl = CampusController()
        researcher_ctrl = ResearcherController()
        group_ctrl = ResearchGroupController()
        area_ctrl = KnowledgeAreaController()
        role_ctrl = RoleController()
        
        # 2. Create University and Campus
        ufsc = uni_ctrl.create_university(name="Federal University of Santa Catarina", short_name="UFSC")
        florianopolis = campus_ctrl.create_campus(name="Florianópolis Campus", organization_id=ufsc.id)
        
        # 3. Create Knowledge Areas
        print("\nCreating Knowledge Areas...")
        ai_area = area_ctrl.create_knowledge_area(name="Artificial Intelligence")
        se_area = area_ctrl.create_knowledge_area(name="Software Engineering")
        print(f"Knowledge Areas: {ai_area.name}, {se_area.name}")
        
        # 4. Create Researchers
        print("\nCreating Researchers...")
        dr_joyce = researcher_ctrl.create_researcher(name="Dr. Joyce", emails=["joyce@ufsc.br"])
        dr_paul = researcher_ctrl.create_researcher(name="Dr. Paul", emails=["paul@ufsc.br"])
        
        # 5. Create Research Group with Metadata and Areas
        print("\nCreating Research Group with Metadata...")
        ai_lab = group_ctrl.create_research_group(
            name="Artificial Intelligence Laboratory",
            campus_id=florianopolis.id,
            organization_id=ufsc.id,
            short_name="LIA",
            cnpq_url="http://dgp.cnpq.br/dgp/espelhogrupo/123",
            site="https://lia.ufsc.br",
            knowledge_area_ids=[ai_area.id, se_area.id]
        )
        print(f"Group created: {ai_lab.name}")
        print(f"CNPq: {ai_lab.cnpq_url}")
        print(f"Site: {ai_lab.site}")
        print(f"Areas: {[a.name for a in ai_lab.knowledge_areas]}")
        
        # 6. Add Leadership (Temporal)
        print("\nAdding Leaders...")
        from datetime import date
        leader_1 = group_ctrl.add_leader(
            team_id=ai_lab.id,
            person_id=dr_joyce.id,
            start_date=date(2023, 1, 1)
        )
        leader_2 = group_ctrl.add_leader(
            team_id=ai_lab.id,
            person_id=dr_paul.id,
            start_date=date(2024, 1, 1)
        )
        print(f"Leaders added to group {ai_lab.name}.")
        
        # 7. Verification
        print("\nVerifying Leadership...")
        leaders = group_ctrl.get_leaders(ai_lab.id)
        print(f"Found {len(leaders)} leaders:")
        for l in leaders:
            print(f"- Person ID: {l.person_id}, Role ID: {l.role_id}, Started: {l.start_date}")
            
    except Exception as e:
        print(f"\nERROR during demo execution: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        print("\n--- Demo Workflow Finished ---")

if __name__ == "__main__":
    run_demo()
