#!/usr/bin/python3

import os
import testinfra.utils.ansible_runner
import urllib3

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_engelsystem(host):
    remote = host.interface('eth0').addresses[0]
    http = urllib3.PoolManager()
    req = http.request('GET', 'http://%s' % remote, headers={
        'Host': 'engel.example.com'
    })
    assert req.headers.get('Server', '').startswith('nginx/')
    assert req.status == 200
    assert b'<title>Login - Engelsystem</title>' in req.data
