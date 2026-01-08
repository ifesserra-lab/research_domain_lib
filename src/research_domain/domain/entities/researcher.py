from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from eo_lib.domain.entities import Person
from eo_lib.domain.base import Base
from typing import Optional, List
from research_domain.domain.mixins import SerializableMixin

# Association Table for Many-to-Many relationship between Researcher and KnowledgeArea
researcher_knowledge_areas = Table(
    "researcher_knowledge_areas",
    Base.metadata,
    Column("researcher_id", Integer, ForeignKey("researchers.id"), primary_key=True),
    Column("area_id", Integer, ForeignKey("knowledge_areas.id"), primary_key=True),
)

class Researcher(Person, SerializableMixin):
    """
    Researcher Model.

    A Researcher represents a person in the research domain, extending eo_lib Person.
    It includes academic metadata like CNPq and Google Scholar links.
    """
    __tablename__ = "researchers"

    id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    cnpq_url = Column(String(255), nullable=True)
    google_scholar_url = Column(String(255), nullable=True)

    # Relationships
    knowledge_areas = relationship(
        "KnowledgeArea",
        secondary=researcher_knowledge_areas,
        lazy="joined"
    )

    def __init__(
        self,
        name: str,
        cnpq_url: Optional[str] = None,
        google_scholar_url: Optional[str] = None,
        knowledge_areas: Optional[List] = None,
        id: Optional[int] = None,
        **kwargs
    ):
        """
        Initializes a new Researcher instance.
        """
        super().__init__(name=name, id=id, **kwargs)
        self.cnpq_url = cnpq_url
        self.google_scholar_url = google_scholar_url
        if knowledge_areas:
            self.knowledge_areas = knowledge_areas
