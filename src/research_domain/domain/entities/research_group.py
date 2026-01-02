from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from eo_lib.domain.entities import Team
from eo_lib.domain.base import Base
from typing import Optional, List

# Association Table for Many-to-Many relationship between ResearchGroup and KnowledgeArea
group_knowledge_areas = Table(
    "group_knowledge_areas",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("research_groups.id"), primary_key=True),
    Column("area_id", Integer, ForeignKey("knowledge_areas.id"), primary_key=True),
)

class ResearchGroup(Team):
    """
    ResearchGroup Model.
    
    A ResearchGroup is a team associated with a campus, extending eo_lib Team.
    It includes research-specific metadata like CNPq links and Knowledge Areas.
    """
    __tablename__ = "research_groups" # Explicitly redefined to handle inheritance correctly in some versions

    id = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    campus_id = Column(Integer, ForeignKey("organizational_units.id"), nullable=True)
    cnpq_url = Column(String(255), nullable=True)
    site = Column(String(255), nullable=True)

    # Relationships
    knowledge_areas = relationship(
        "KnowledgeArea",
        secondary=group_knowledge_areas,
        lazy="joined"
    )

    def __init__(
        self,
        name: str,
        campus_id: Optional[int] = None,
        description: Optional[str] = None,
        short_name: Optional[str] = None,
        organization_id: Optional[int] = None,
        cnpq_url: Optional[str] = None,
        site: Optional[str] = None,
        knowledge_areas: Optional[List] = None,
        id: Optional[int] = None,
    ):
        """
        Initializes a new ResearchGroup instance.
        """
        super().__init__(
            name=name,
            description=description,
            short_name=short_name,
            organization_id=organization_id,
            id=id,
        )
        self.campus_id = campus_id
        self.cnpq_url = cnpq_url
        self.site = site
        if knowledge_areas:
            self.knowledge_areas = knowledge_areas
