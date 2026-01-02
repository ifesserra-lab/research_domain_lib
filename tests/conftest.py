import pytest

@pytest.fixture
def service_factory():
    from research_domain.factories import ServiceFactory
    return ServiceFactory()
