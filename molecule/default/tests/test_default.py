import os

# import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_engine_accessible(host):
    result = host.run('docker info --format "{{.ServerVersion}}"')
    assert result.rc == 0
    assert result.stdout.strip()


def test_syncserver_container_running(host):
    result = host.run(
        'docker inspect --format "{{.State.Running}}" mozilla-syncserver'
    )
    assert result.rc == 0
    assert result.stdout.strip() == 'true'
