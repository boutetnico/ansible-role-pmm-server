ansible-role-pmm-server
=======================

This role installs PMM server using the [official Docker image](https://hub.docker.com/r/percona/pmm-server).

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Role Variables
--------------

| Variable                        | Required | Default              | Choices | Comments                                           |
|---------------------------------|----------|----------------------|---------|----------------------------------------------------|
| pmm_server_docker_image_name    | true     | `percona/pmm-server` | string  |                                                    |
| pmm_server_docker_image_version | true     | `2`                  | string  |                                                    |
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

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-9
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1604
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
