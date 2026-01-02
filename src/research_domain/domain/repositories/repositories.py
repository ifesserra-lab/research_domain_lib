from libbase.infrastructure.interface import IRepository as GenericRepositoryInterface
from eo_lib.domain.repositories import (
    PersonRepositoryInterface,
    OrganizationRepositoryInterface,
    OrganizationalUnitRepositoryInterface,
    TeamRepositoryInterface,
)
from eo_lib.domain.entities import (
    Person,
    Team,
    Organization,
    OrganizationalUnit,
    Role,
)
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    KnowledgeArea,
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

class KnowledgeAreaRepositoryInterface(GenericRepositoryInterface):
    """Interface for KnowledgeArea Repository."""
    pass

class RoleRepositoryInterface(GenericRepositoryInterface):
    """Interface for Role Repository."""
    pass
