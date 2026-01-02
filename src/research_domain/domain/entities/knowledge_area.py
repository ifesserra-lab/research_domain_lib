from sqlalchemy import Column, Integer, String
from eo_lib.domain.base import Base
from typing import Optional

class KnowledgeArea(Base):
    """
    KnowledgeArea Model.
    
    Represents a thematic area or field of study for research groups.
    """
    __tablename__ = "knowledge_areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    def __init__(self, name: str, id: Optional[int] = None):
        """
        Initializes a new KnowledgeArea instance.
        
        Args:
            name (str): Unique name of the knowledge area.
            id (int, optional): Database ID for existing records.
        """
        self.name = name
        if id:
            self.id = id
