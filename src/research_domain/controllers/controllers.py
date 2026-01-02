from typing import List, Optional
from datetime import date
from libbase.controllers.generic_controller import GenericController
from eo_lib.domain.entities import Role, TeamMember
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    KnowledgeArea,
)
from research_domain.factories import ServiceFactory

class ResearcherController(GenericController[Researcher]):
    def __init__(self):
        service = ServiceFactory.create_researcher_service()
        super().__init__(service)

    def create_researcher(
        self,
        name: str,
        emails: List[str] = None,
        identification_id: str = None,
        birthday: date = None,
    ) -> Researcher:
        return self._service.create_with_details(name, emails, identification_id, birthday)

class UniversityController(GenericController[University]):
    def __init__(self):
        service = ServiceFactory.create_university_service()
        super().__init__(service)

    def create_university(
        self,
        name: str,
        description: str = None,
        short_name: str = None,
    ) -> University:
        university = University(name=name, description=description, short_name=short_name)
        self.create(university)
        return university

class CampusController(GenericController[Campus]):
    def __init__(self):
        service = ServiceFactory.create_campus_service()
        super().__init__(service)

    def create_campus(
        self,
        name: str,
        organization_id: int,
        description: str = None,
        short_name: str = None,
    ) -> Campus:
        campus = Campus(name=name, organization_id=organization_id, description=description, short_name=short_name)
        self.create(campus)
        return campus

class KnowledgeAreaController(GenericController[KnowledgeArea]):
    def __init__(self):
        service = ServiceFactory.create_knowledge_area_service()
        super().__init__(service)

    def create_knowledge_area(self, name: str) -> KnowledgeArea:
        area = KnowledgeArea(name=name)
        self.create(area)
        return area

class RoleController(GenericController[Role]):
    def __init__(self):
        service = ServiceFactory.create_role_service()
        super().__init__(service)

    def create_role(self, name: str, description: str = None) -> Role:
        role = Role(name=name, description=description)
        self.create(role)
        return role

    def get_or_create_leader_role(self) -> Role:
        return self._service.get_or_create_leader_role()

class ResearchGroupController(GenericController[ResearchGroup]):
    def __init__(self):
        service = ServiceFactory.create_research_group_service()
        super().__init__(service)
        self._area_service = ServiceFactory.create_knowledge_area_service()
        self._role_service = ServiceFactory.create_role_service()

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
        cnpq_url: str = None,
        site: str = None,
        knowledge_area_ids: List[int] = None,
    ) -> ResearchGroup:
        areas = []
        if knowledge_area_ids:
            for aid in knowledge_area_ids:
                area = self._area_service.get_by_id(aid)
                if area:
                    areas.append(area)
        
        return self._service.create_research_group(
            name=name,
            campus_id=campus_id,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
            cnpq_url=cnpq_url,
            site=site,
            knowledge_areas=areas,
        )

    def add_leader(
        self,
        team_id: int,
        person_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> TeamMember:
        leader_role = self._role_service.get_or_create_leader_role()
        return self._service.add_leader(
            team_id=team_id,
            person_id=person_id,
            role_id=leader_role.id,
            start_date=start_date,
            end_date=end_date,
        )
        
    def get_leaders(self, team_id: int) -> List[TeamMember]:
        members = self._service.get_members(team_id)
        leader_role = self._role_service.get_or_create_leader_role()
        return [m for m in members if m.role_id == leader_role.id]
