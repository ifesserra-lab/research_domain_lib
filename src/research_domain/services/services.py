from typing import List, Optional
from datetime import date
from eo_lib.services import (
    PersonService,
    OrganizationService,
    OrganizationalUnitService,
    TeamService,
)
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    ResearcherInGroup,
)
from research_domain.domain.repositories import (
    ResearcherRepositoryInterface,
    UniversityRepositoryInterface,
    CampusRepositoryInterface,
    ResearchGroupRepositoryInterface,
)

class ResearcherService(PersonService):
    def __init__(self, repo: ResearcherRepositoryInterface):
        super().__init__(repo)

class UniversityService(OrganizationService):
    def __init__(self, repo: UniversityRepositoryInterface):
        super().__init__(repo)

class CampusService(OrganizationalUnitService):
    def __init__(self, repo: CampusRepositoryInterface):
        super().__init__(repo)

class ResearchGroupService(TeamService):
    def __init__(self, repo: ResearchGroupRepositoryInterface):
        super().__init__(repo)

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
    ) -> ResearchGroup:
        group = ResearchGroup(
            name=name,
            campus_id=campus_id,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
        )
        self.create(group)
        return group
