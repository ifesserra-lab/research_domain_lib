from sqlalchemy import Column, Integer, ForeignKey
from eo_lib.domain.entities import Team, TeamMember

class ResearchGroup(Team):
    """A ResearchGroup is a team associated with a campus, extending eo_lib Team."""
    campus_id = Column(Integer, ForeignKey("organizational_units.id"), nullable=True)

    def __init__(
        self,
        name: str,
        campus_id: int = None,
        description: str = None,
        short_name: str = None,
        organization_id: int = None,
        id: int = None,
    ):
        super().__init__(
            name=name,
            description=description,
            short_name=short_name,
            organization_id=organization_id,
            id=id,
        )
        self.campus_id = campus_id

class ResearcherInGroup(TeamMember):
    """Association between a Researcher and a ResearchGroup, extending eo_lib TeamMember."""
    pass
