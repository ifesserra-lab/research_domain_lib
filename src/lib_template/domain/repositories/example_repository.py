from abc import ABC
from libbase.domain.repositories.base import BaseRepository
from ..entities.example import Example

class ExampleRepository(BaseRepository[Example], ABC):
    """Interface for Example repository."""
    pass
