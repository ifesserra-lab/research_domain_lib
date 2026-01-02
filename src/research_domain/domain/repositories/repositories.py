from eo_lib.domain.repositories import (
    PersonRepositoryInterface,
    OrganizationRepositoryInterface,
    OrganizationalUnitRepositoryInterface,
    TeamRepositoryInterface,
)
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
)

class ResearcherRepositoryInterface(PersonRepositoryInterface):
    """Interface for Researcher Repository."""
    pass

class UniversityRepositoryInterface(OrganizationRepositoryInterface):
    """Interface for University Repository."""
    pass

class CampusRepositoryInterface(OrganizationalUnitRepositoryInterface):
    """Interface for Campus Repository."""
    pass

class ResearchGroupRepositoryInterface(TeamRepositoryInterface):
    """Interface for ResearchGroup Repository."""
    pass
