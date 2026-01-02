from .sql_repositories import (
    PostgresResearcherRepository,
    PostgresUniversityRepository,
    PostgresCampusRepository,
    PostgresResearchGroupRepository,
)
from .memory_repositories import (
    InMemoryResearcherRepository,
    InMemoryUniversityRepository,
    InMemoryCampusRepository,
    InMemoryResearchGroupRepository,
)

__all__ = [
    "PostgresResearcherRepository",
    "PostgresUniversityRepository",
    "PostgresCampusRepository",
    "PostgresResearchGroupRepository",
    "InMemoryResearcherRepository",
    "InMemoryUniversityRepository",
    "InMemoryCampusRepository",
    "InMemoryResearchGroupRepository",
]
