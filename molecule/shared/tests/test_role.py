import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


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
