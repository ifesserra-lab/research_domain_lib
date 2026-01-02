from .controllers import (
    ResearcherController,
    UniversityController,
    CampusController,
    ResearchGroupController,
)
from .domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    ResearcherInGroup,
)
from .services import (
    ResearcherService,
    UniversityService,
    CampusService,
    ResearchGroupService,
)

__all__ = [
    "ResearcherController",
    "UniversityController",
    "CampusController",
    "ResearchGroupController",
    "Researcher",
    "University",
    "Campus",
    "ResearchGroup",
    "ResearcherInGroup",
    "ResearcherService",
    "UniversityService",
    "CampusService",
    "ResearchGroupService",
]
