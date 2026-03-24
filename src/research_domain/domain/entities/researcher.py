from typing import List, Optional

from eo_lib.domain.base import Base
from eo_lib.domain.entities import Person
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin
from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.entities.proficiency import Proficiency
from research_domain.domain.entities.award import Award

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
    resume = Column(Text, nullable=True)
    citation_names = Column(String(500), nullable=True)

    # Relationships
    knowledge_areas = relationship(
        "KnowledgeArea", secondary=researcher_knowledge_areas, lazy="joined"
    )
    academic_educations = relationship(
        "AcademicEducation",
        back_populates="researcher",
        cascade="all, delete-orphan",
        foreign_keys=[AcademicEducation.researcher_id]
    )
    proficiencies = relationship(
        "Proficiency",
        back_populates="researcher",
        cascade="all, delete-orphan"
    )
    awards = relationship(
        "Award",
        back_populates="researcher",
        cascade="all, delete-orphan"
    )
    articles = relationship(
        "Article",
        secondary="article_authors", 
        back_populates="authors",
        lazy="joined"
    )
    productions = relationship(
        "ResearchProduction",
        secondary="production_authors",
        back_populates="authors",
        lazy="joined"
    )

    def __init__(
        self,
        name: str,
        cnpq_url: Optional[str] = None,
        google_scholar_url: Optional[str] = None,
        resume: Optional[str] = None,
        citation_names: Optional[str] = None,
        knowledge_areas: Optional[List] = None,
        articles: Optional[List] = None,
        id: Optional[int] = None,
        **kwargs,
    ):
        """
        Initializes a new Researcher instance.
        """
        super().__init__(name=name, id=id, **kwargs)
        self.cnpq_url = cnpq_url
        self.google_scholar_url = google_scholar_url
        self.resume = resume
        self.citation_names = citation_names
        
        if knowledge_areas:
            self.knowledge_areas = knowledge_areas
        if articles:
            self.articles = articles
