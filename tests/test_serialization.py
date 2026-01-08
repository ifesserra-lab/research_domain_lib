
import pytest
from research_domain.domain.entities.research_group import ResearchGroup
from research_domain.domain.entities.researcher import Researcher

def test_research_group_serialization_includes_parent_data():
    """
    Test that ResearchGroup (which inherits from Team) includes Team attributes
    in its dictionary representation.
    """
    group = ResearchGroup(
        name="Quantum Computing Group",  # Parent (Team) attribute
        campus_id=10,                    # Child (ResearchGroup) attribute
        description="Exploring Qubits",  # Parent (Team) attribute
        cnpq_url="http://cnpq/qc"        # Child (ResearchGroup) attribute
    )
    
    # This method is expected to be implemented
    data = group.to_dict()
    
    # Check Parent fields
    assert "name" in data
    assert data["name"] == "Quantum Computing Group"
    assert "description" in data
    assert data["description"] == "Exploring Qubits"
    
    # Check Child fields
    assert "campus_id" in data
    assert data["campus_id"] == 10
    assert "cnpq_url" in data
    assert data["cnpq_url"] == "http://cnpq/qc"

def test_researcher_serialization_includes_parent_data():
    """
    Test that Researcher (which inherits from Person) includes Person attributes.
    """
    researcher = Researcher(
        name="Dr. Banner",              # Parent (Person) attribute
        cnpq_url="http://lattes/hulk"   # Child (Researcher) attribute
    )
    
    data = researcher.to_dict()
    
    assert "name" in data
    assert data["name"] == "Dr. Banner"
    assert "cnpq_url" in data
    assert data["cnpq_url"] == "http://lattes/hulk"
