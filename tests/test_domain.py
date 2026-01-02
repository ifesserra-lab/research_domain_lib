import pytest
from datetime import date
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.entities.university import University, Campus
from research_domain.domain.entities.research_group import ResearchGroup
from research_domain.domain.entities.knowledge_area import KnowledgeArea
from eo_lib.domain.entities import TeamMember, Role

def test_create_university():
    uni = University(name="Federal University", short_name="UFSC")
    assert uni.name == "Federal University"
    assert uni.short_name == "UFSC"

def test_create_campus():
    campus = Campus(name="Main Campus", organization_id=1)
    assert campus.name == "Main Campus"
    assert campus.organization_id == 1

def test_create_researcher():
    researcher = Researcher(name="Dr. Smith")
    assert researcher.name == "Dr. Smith"

def test_create_knowledge_area():
    area = KnowledgeArea(name="Artificial Intelligence")
    assert area.name == "Artificial Intelligence"

def test_create_research_group_with_metadata():
    group = ResearchGroup(
        name="AI Lab",
        campus_id=1,
        cnpq_url="http://cnpq.br/123",
        site="http://ai.ufsc.br"
    )
    assert group.name == "AI Lab"
    assert group.cnpq_url == "http://cnpq.br/123"
    assert group.site == "http://ai.ufsc.br"

def test_research_group_many_to_many_knowledge_areas():
    area1 = KnowledgeArea(name="AI", id=1)
    area2 = KnowledgeArea(name="Software Engineering", id=2)
    
    group = ResearchGroup(
        name="Advanced Lab",
        knowledge_areas=[area1, area2]
    )
    
    assert len(group.knowledge_areas) == 2
    assert area1 in group.knowledge_areas
    assert area2 in group.knowledge_areas

def test_team_member_temporal_leadership():
    # Role entity from eo_lib
    leader_role = Role(name="Leader", id=1)
    
    # TeamMember with temporal dates
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    
    membership = TeamMember(
        person_id=1,
        team_id=1,
        role_id=leader_role.id,
        start_date=start,
        end_date=end
    )
    
    assert membership.role_id == 1
    assert membership.start_date == start
    assert membership.end_date == end

def test_add_researcher_to_group_basic():
    # Using strictly eo_lib TeamMember
    membership = TeamMember(
        person_id=1,
        team_id=1,
        role_id=2, # Researcher Role
        start_date=date.today()
    )
    assert membership.person_id == 1
    assert membership.team_id == 1
    assert membership.role_id == 2
    assert membership.start_date == date.today()
