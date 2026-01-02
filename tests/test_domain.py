import pytest
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.entities.university import University, Campus
from research_domain.domain.entities.research_group import ResearchGroup, ResearcherInGroup

def test_create_university():
    uni = University(name="Federal University")
    assert uni.name == "Federal University"

def test_create_campus():
    uni = University(name="Federal University", id=1)
    campus = Campus(name="Main Campus", organization_id=uni.id)
    assert campus.name == "Main Campus"
    assert campus.organization_id == 1

def test_create_researcher():
    researcher = Researcher(name="Dr. Smith")
    assert researcher.name == "Dr. Smith"

def test_create_research_group():
    uni = University(name="Federal University", id=1)
    campus = Campus(name="Main Campus", organization_id=uni.id, id=1)
    group = ResearchGroup(name="AI Lab", campus_id=campus.id, organization_id=uni.id)
    assert group.name == "AI Lab"
    assert group.campus_id == 1
    assert group.organization_id == 1

def test_add_researcher_to_group():
    researcher = Researcher(name="Dr. Smith", id=1)
    group = ResearchGroup(name="AI Lab", campus_id=1, id=1)
    # ResearcherInGroup inherits from TeamMember
    membership = ResearcherInGroup(person_id=researcher.id, team_id=group.id, role="Lead Researcher")
    assert membership.person_id == 1
    assert membership.team_id == 1
    # Role is handled by TeamMember constructor (it might create a Role object or just store it)
    # Let's check if membership.role exists or if we should check role name
    assert membership.role is not None
