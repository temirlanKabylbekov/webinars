import pytest

pytest_plugins = [
    'fixtures.rand'
]


@pytest.fixture
def global_fixture():
    return 'global fixture'
