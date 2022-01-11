[![tests](https://github.com/boutetnico/ansible-role-pmm-server/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-pmm-server/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.pmm_server-blue.svg)](https://galaxy.ansible.com/boutetnico/pmm_server)

ansible-role-pmm-server
=======================

This role installs [PMM server](https://www.percona.com/doc/percona-monitoring-and-management/2.x/introduction.html) using the [official Docker image](https://hub.docker.com/r/percona/pmm-server).

It is part of a family of Ansible roles allowing to setup and configure PMM:

- [ansible-role-pmm-server](https://github.com/boutetnico/ansible-role-pmm-server)
- [ansible-role-pmm-client](https://github.com/boutetnico/ansible-role-pmm-client)

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                        | Required | Default              | Choices | Comments                                           |
|---------------------------------|----------|----------------------|---------|----------------------------------------------------|
| pmm_server_docker_image_name    | true     | `percona/pmm-server` | string  |                                                    |
| pmm_server_docker_image_version | true     | `2`                  | string  |                                                    |
| pmm_server_docker_pull          | true     | `false`              | boolean | Set `true` to force pulling a newer Docker image.  |
| pmm_server_docker_env           | true     | `{}`                 | dict    |                                                    |
| pmm_server_network_mode         | true     | `bridge`             | string  | `bridge`, `host`, `none` or `container:<name|id>`. |
| pmm_server_ports                | true     |                      | list    | See `defaults/main.yml`.                           |
| pmm_server_container_state      | true     | `started`            | string  | `absent`, `present`, `stopped` or `started`.       |
| pmm_server_restart_policy       | true     | `unless-stopped`     | string  |                                                    |
| pmm_server_anonymous_access     | true     | `false`              | bool    | Enable or disable anonymous dashboard access.      |

Dependencies
------------

Docker

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-pmm-server

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-11

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2004

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
