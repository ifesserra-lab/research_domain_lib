from typing import List, Optional
from datetime import date
from libbase.services.generic_service import GenericService
from eo_lib.services import (
    PersonService,
    OrganizationService,
    OrganizationalUnitService,
    TeamService,
)
from eo_lib.domain.entities import TeamMember, Role
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    KnowledgeArea,
)
from research_domain.domain.repositories import (
    ResearcherRepositoryInterface,
    UniversityRepositoryInterface,
    CampusRepositoryInterface,
    ResearchGroupRepositoryInterface,
    KnowledgeAreaRepositoryInterface,
    RoleRepositoryInterface,
)

class RoleService(GenericService[Role]):
    def __init__(self, repo: RoleRepositoryInterface):
        super().__init__(repo)
        self.repo = repo

    def get_or_create_leader_role(self) -> Role:
        """Finds or creates the 'Leader' role."""
        roles = self.get_all()
        for r in roles:
            if r.name.lower() == "leader":
                return r
        
        leader_role = Role(name="Leader", description="Research Group Leader")
        self.create(leader_role)
        return leader_role

class KnowledgeAreaService(GenericService[KnowledgeArea]):
    def __init__(self, repo: KnowledgeAreaRepositoryInterface):
        super().__init__(repo)

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
        self.repo = repo

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
        cnpq_url: str = None,
        site: str = None,
        knowledge_areas: List[KnowledgeArea] = None,
    ) -> ResearchGroup:
        group = ResearchGroup(
            name=name,
            campus_id=campus_id,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
            cnpq_url=cnpq_url,
            site=site,
            knowledge_areas=knowledge_areas,
        )
        self.create(group)
        return group

    def add_leader(
        self,
        team_id: int,
        person_id: int,
        role_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> TeamMember:
        """Adds a leader to the group."""
        if not start_date:
            start_date = date.today()
        
        return self.add_member(
            team_id=team_id,
            person_id=person_id,
            role_id=role_id,
            start_date=start_date,
            end_date=end_date,
        )
