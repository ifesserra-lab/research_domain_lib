from typing import List, Optional
from datetime import date
from libbase.controllers.generic_controller import GenericController
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
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

class ResearchGroupController(GenericController[ResearchGroup]):
    def __init__(self):
        service = ServiceFactory.create_research_group_service()
        super().__init__(service)

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
    ) -> ResearchGroup:
        return self._service.create_research_group(
            name, campus_id, organization_id, description, short_name
        )
