from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryResearcherRepository,
    InMemoryUniversityRepository,
    InMemoryCampusRepository,
    InMemoryResearchGroupRepository,
    InMemoryKnowledgeAreaRepository,
    InMemoryRoleRepository,
    PostgresResearcherRepository,
    PostgresUniversityRepository,
    PostgresCampusRepository,
    PostgresResearchGroupRepository,
    PostgresKnowledgeAreaRepository,
    PostgresRoleRepository,
)
from research_domain.services import (
    ResearcherService,
    UniversityService,
    CampusService,
    ResearchGroupService,
    KnowledgeAreaService,
    RoleService,
)

class ServiceFactory:
    """
    Factory for creating Service instances with the appropriate Repository Strategy.
    """
    @staticmethod
    def _get_strategies():
        t = Config.get_storage_type().lower()
        if t in ["postgres", "db"]:
            return (
                PostgresResearcherRepository,
                PostgresUniversityRepository,
                PostgresCampusRepository,
                PostgresResearchGroupRepository,
                PostgresKnowledgeAreaRepository,
                PostgresRoleRepository,
            )
        # Default to memory
        return (
            InMemoryResearcherRepository,
            InMemoryUniversityRepository,
            InMemoryCampusRepository,
            InMemoryResearchGroupRepository,
            InMemoryKnowledgeAreaRepository,
            InMemoryRoleRepository,
        )

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        (ResearcherRepo, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearcherService(ResearcherRepo())

    @staticmethod
    def create_university_service() -> UniversityService:
        (_, UniversityRepo, _, _, _, _) = ServiceFactory._get_strategies()
        return UniversityService(UniversityRepo())

    @staticmethod
    def create_campus_service() -> CampusService:
        (_, _, CampusRepo, _, _, _) = ServiceFactory._get_strategies()
        return CampusService(CampusRepo())

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        (_, _, _, GroupRepo, _, _) = ServiceFactory._get_strategies()
        return ResearchGroupService(GroupRepo())

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        (_, _, _, _, AreaRepo, _) = ServiceFactory._get_strategies()
        return KnowledgeAreaService(AreaRepo())

    @staticmethod
    def create_role_service() -> RoleService:
        (_, _, _, _, _, RoleRepo) = ServiceFactory._get_strategies()
        return RoleService(RoleRepo())
