import pytest


@pytest.mark.parametrize(
    "name,running",
    [
        ("pmm-data", False),
        ("pmm-server", True),
    ],
)
def test_pmm_container(host, name, running):
    container = host.docker(name)
    assert container.name == name
    assert container.is_running == running
