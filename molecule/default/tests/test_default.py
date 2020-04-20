import os
import pytest


import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

mytruth = True
@pytest.mark.parametrize('pkg', [
  'httpd',
  'firewalld'
])

def mytest(host,pkg):
    print(host)
    print("installed or not?", pkg.is_installed)
    assert mytruth