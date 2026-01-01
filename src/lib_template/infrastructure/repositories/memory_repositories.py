from lib_template.domain.repositories import ExampleRepository
from lib_template.domain.entities import Example
from libbase.infrastructure.memory_repository import GenericMemoryRepository

class InMemoryExampleRepository(GenericMemoryRepository[Example], ExampleRepository):
    """
    In-Memory implementation of the Example Repository.
    """
    def __init__(self):
        super().__init__(Example)
