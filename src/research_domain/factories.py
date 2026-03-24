from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAdvisorshipRepository, InMemoryArticleRepository,
    InMemoryCampusRepository, InMemoryEducationTypeRepository,
    InMemoryFellowshipRepository, InMemoryKnowledgeAreaRepository,
    InMemoryProductionTypeRepository, InMemoryResearchProductionRepository,
    InMemoryResearcherRepository, InMemoryResearchGroupRepository,
    InMemoryRoleRepository, InMemoryUniversityRepository,
    InMemoryAcademicEducationRepository,
    PostgresAcademicEducationRepository, PostgresAdvisorshipRepository,
    PostgresArticleRepository, PostgresCampusRepository,
    PostgresEducationTypeRepository, PostgresFellowshipRepository,
    PostgresKnowledgeAreaRepository, PostgresProductionTypeRepository,
    PostgresResearchProductionRepository, PostgresResearcherRepository,
    PostgresResearchGroupRepository, PostgresRoleRepository,
    PostgresUniversityRepository)
from research_domain.services import (
    AcademicEducationService, AdvisorshipService, ArticleService,
    CampusService, EducationTypeService, FellowshipService,
    KnowledgeAreaService, ProductionTypeService, ResearchProductionService,
    ResearcherService, ResearchGroupService,
    RoleService, UniversityService)


class ServiceFactory:
    """
    Factory for creating Service instances with the appropriate Repository Strategy.
    """

    _memory_repo_instances = {}

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
                PostgresAdvisorshipRepository,
                PostgresFellowshipRepository,
                PostgresAcademicEducationRepository,
                PostgresArticleRepository,
                PostgresEducationTypeRepository,
                PostgresProductionTypeRepository,
                PostgresResearchProductionRepository,
            )
        # Default to memory
        return (
            InMemoryResearcherRepository,
            InMemoryUniversityRepository,
            InMemoryCampusRepository,
            InMemoryResearchGroupRepository,
            InMemoryKnowledgeAreaRepository,
            InMemoryRoleRepository,
            InMemoryAdvisorshipRepository,
            InMemoryFellowshipRepository,
            InMemoryAcademicEducationRepository,
            InMemoryArticleRepository,
            InMemoryEducationTypeRepository,
            InMemoryProductionTypeRepository,
            InMemoryResearchProductionRepository,
        )

    @classmethod
    def _build_repository(cls, repo_type):
        if Config.get_storage_type().lower() in ["postgres", "db"]:
            return repo_type()

        if repo_type not in cls._memory_repo_instances:
            cls._memory_repo_instances[repo_type] = repo_type()
        return cls._memory_repo_instances[repo_type]

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        (ResearcherRepo, _, _, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearcherService(ServiceFactory._build_repository(ResearcherRepo))

    @staticmethod
    def create_university_service() -> UniversityService:
        (_, UniversityRepo, _, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return UniversityService(ServiceFactory._build_repository(UniversityRepo))

    @staticmethod
    def create_campus_service() -> CampusService:
        (_, _, CampusRepo, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return CampusService(ServiceFactory._build_repository(CampusRepo))

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        (_, _, _, GroupRepo, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearchGroupService(ServiceFactory._build_repository(GroupRepo))

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        (_, _, _, _, AreaRepo, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return KnowledgeAreaService(ServiceFactory._build_repository(AreaRepo))

    @staticmethod
    def create_role_service() -> RoleService:
        (_, _, _, _, _, RoleRepo, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return RoleService(ServiceFactory._build_repository(RoleRepo))

    @staticmethod
    def create_advisorship_service() -> AdvisorshipService:
        (
            ResearcherRepo,
            _,
            _,
            _,
            _,
            RoleRepo,
            AdvisorshipRepo,
            _,
            _,
            _,
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return AdvisorshipService(
            repo=ServiceFactory._build_repository(AdvisorshipRepo),
            researcher_repo=ServiceFactory._build_repository(ResearcherRepo),
            role_repo=ServiceFactory._build_repository(RoleRepo),
        )

    @staticmethod
    def create_fellowship_service() -> FellowshipService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            FellowshipRepo,
            _,
            _,
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return FellowshipService(ServiceFactory._build_repository(FellowshipRepo))

    @staticmethod
    def create_academic_education_service() -> AcademicEducationService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            AcademicEducationRepo,
            _,
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return AcademicEducationService(
            ServiceFactory._build_repository(AcademicEducationRepo)
        )

    @staticmethod
    def create_article_service() -> ArticleService:
        (
            ResearcherRepo,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            ArticleRepo,
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return ArticleService(
            ServiceFactory._build_repository(ArticleRepo),
            ServiceFactory._build_repository(ResearcherRepo),
        )

    @staticmethod
    def create_education_type_service() -> EducationTypeService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            EducationTypeRepo,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return EducationTypeService(
            ServiceFactory._build_repository(EducationTypeRepo)
        )

    @staticmethod
    def create_production_type_service() -> ProductionTypeService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            ProductionTypeRepo,
            _,
        ) = ServiceFactory._get_strategies()
        return ProductionTypeService(
            ServiceFactory._build_repository(ProductionTypeRepo)
        )

    @staticmethod
    def create_research_production_service() -> ResearchProductionService:
        (
            ResearcherRepo,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            ProductionRepo,
        ) = ServiceFactory._get_strategies()
        return ResearchProductionService(
            ServiceFactory._build_repository(ProductionRepo),
            ServiceFactory._build_repository(ResearcherRepo),
        )
