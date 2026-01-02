from .sql_repositories import (
    PostgresResearcherRepository,
    PostgresUniversityRepository,
    PostgresCampusRepository,
    PostgresResearchGroupRepository,
    PostgresKnowledgeAreaRepository,
    PostgresRoleRepository,
)
from .memory_repositories import (
    InMemoryResearcherRepository,
    InMemoryUniversityRepository,
    InMemoryCampusRepository,
    InMemoryResearchGroupRepository,
    InMemoryKnowledgeAreaRepository,
    InMemoryRoleRepository,
)

__all__ = [
    "PostgresResearcherRepository",
    "PostgresUniversityRepository",
    "PostgresCampusRepository",
    "PostgresResearchGroupRepository",
    "PostgresKnowledgeAreaRepository",
    "PostgresRoleRepository",
    "InMemoryResearcherRepository",
    "InMemoryUniversityRepository",
    "InMemoryCampusRepository",
    "InMemoryResearchGroupRepository",
    "InMemoryKnowledgeAreaRepository",
    "InMemoryRoleRepository",
]
