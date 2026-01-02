from eo_lib.domain.entities import Organization, OrganizationalUnit

class University(Organization):
    """A University is an organization, extending eo_lib Organization."""
    pass

class Campus(OrganizationalUnit):
    """A Campus is an organizational unit within a university, extending eo_lib OrganizationalUnit."""
    pass
