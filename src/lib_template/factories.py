from lib_template.config import Config
from lib_template.infrastructure.repositories import InMemoryExampleRepository
from lib_template.services import ExampleService

class ServiceFactory:
    """
    Factory for creating Service instances with the appropriate Repository Strategy.
    """
    @staticmethod
    def _get_strategies():
        t = Config.get_storage_type().lower()
        # simplified strategy selection for template
        if t == "memory":
            return (InMemoryExampleRepository,)
        return (InMemoryExampleRepository,)

    @staticmethod
    def create_example_service() -> ExampleService:
        (RepoClass,) = ServiceFactory._get_strategies()
        return ExampleService(RepoClass())
