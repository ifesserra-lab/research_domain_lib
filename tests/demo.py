import os
from sqlalchemy import text
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from eo_lib.domain.base import Base

# Try to load .env for local configuration (e.g., STORAGE_TYPE=postgres)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import all research domain entities to ensure they are registered with Base metadata
from research_domain import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    ResearcherInGroup,
    ResearcherController,
    UniversityController,
    CampusController,
    ResearchGroupController,
)

# Also import eo_lib entities as requested
from eo_lib.domain.entities import (
    Person,
    PersonEmail,
    Team,
    TeamMember,
    Initiative,
    InitiativeType,
    Organization,
    OrganizationalUnit,
)

def setup_database():
    """
    Initializes the database by dropping and recreating all tables.
    Matches the user's requested logic.
    """
    storage_type = os.getenv("STORAGE_TYPE", "memory").lower()
    if storage_type not in ["postgres", "db"]:
        print(f"Skipping database initialization (STORAGE_TYPE is '{storage_type}', not 'postgres' or 'db').")
        return

    print("Initializing Database Tables...")
    client = PostgresClient()
    
    # Drop legacy tables to clean old schema as requested
    try:
        with client._engine.connect() as conn:
            print("Dropping legacy tables (project_teams, project_persons, projects)...")
            conn.execute(text("DROP TABLE IF EXISTS project_teams CASCADE"))
            conn.execute(text("DROP TABLE IF EXISTS project_persons CASCADE"))
            conn.execute(text("DROP TABLE IF EXISTS projects CASCADE"))
            conn.commit()
    except Exception as e:
        print(f"Note: Potential error dropping legacy tables (ignored): {e}")

    print("Dropping and recreating all tables via Base.metadata...")
    Base.metadata.drop_all(client._engine)
    Base.metadata.create_all(client._engine)
    print("Database tables initialized successfully.")

def run_demo():
    """
    Executes the demonstration workflow.
    """
    print("--- Starting ResearchDomain Demo ---")
    
    # Initialize Database if Postgres is selected
    setup_database()
    
    try:
        # 1. Initialize Controllers
        uni_ctrl = UniversityController()
        campus_ctrl = CampusController()
        researcher_ctrl = ResearcherController()
        group_ctrl = ResearchGroupController()
        
        # 2. Create University
        print("\nCreating University...")
        ufsc = uni_ctrl.create_university(name="Federal University of Santa Catarina", short_name="UFSC")
        print(f"University created: {ufsc.name} (ID: {ufsc.id})")
        
        # 3. Create Campus
        print("\nCreating Campus...")
        florianopolis = campus_ctrl.create_campus(name="Florianópolis Campus", organization_id=ufsc.id)
        print(f"Campus created: {florianopolis.name} (ID: {florianopolis.id})")
        
        # 4. Create Researcher
        print("\nCreating Researcher...")
        dr_joyce = researcher_ctrl.create_researcher(name="Dr. Joyce", emails=["joyce@ufsc.br"])
        print(f"Researcher created: {dr_joyce.name} (ID: {dr_joyce.id})")
        
        # 5. Create Research Group
        print("\nCreating Research Group...")
        ai_lab = group_ctrl.create_research_group(
            name="Artificial Intelligence Laboratory",
            campus_id=florianopolis.id,
            organization_id=ufsc.id,
            short_name="LIA"
        )
        print(f"Research Group created: {ai_lab.name} (ID: {ai_lab.id})")
        
        # 6. List all and verify
        print("\nVerifying data...")
        groups = group_ctrl.get_all()
        print(f"Total Research Groups found: {len(groups)}")
        for g in groups:
            print(f"- {g.name} ({g.short_name}) [Campus ID: {g.campus_id}]")
            
    except Exception as e:
        print(f"\nERROR during demo execution: {e}")
        raise
    finally:
        print("\n--- Demo Workflow Finished ---")

if __name__ == "__main__":
    run_demo()
