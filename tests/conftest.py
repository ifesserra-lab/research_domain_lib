import pytest
from lib_template.factories import ServiceFactory

@pytest.fixture
def example_service():
    return ServiceFactory.create_example_service()
