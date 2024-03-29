# Ansible role [mozilla_syncserver](https://galaxy.ansible.com/ui/standalone/roles/buluma/mozilla_syncserver/documentation)

A deployment role for Mozilla's Firefox Sync server.

|GitHub|Version|Issues|Pull Requests|Downloads|
|------|-------|------|-------------|---------|
|[![github](https://github.com/buluma/ansible-role-mozilla_syncserver/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-mozilla_syncserver/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-mozilla_syncserver.svg)](https://github.com/buluma/ansible-role-mozilla_syncserver/releases/)|[![Issues](https://img.shields.io/github/issues/buluma/ansible-role-mozilla_syncserver.svg)](https://github.com/buluma/ansible-role-mozilla_syncserver/issues/)|[![PullRequests](https://img.shields.io/github/issues-pr-closed-raw/buluma/ansible-role-mozilla_syncserver.svg)](https://github.com/buluma/ansible-role-mozilla_syncserver/pulls/)|[![Ansible Role](https://img.shields.io/ansible/role/d/buluma/mozilla_syncserver)](https://galaxy.ansible.com/ui/standalone/roles/buluma/mozilla_syncserver/documentation)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  tasks:
    - name: "Include ansible-mozilla-syncserver"
      include_role:
        name: "buluma.mozilla_syncserver"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  pre_tasks:
    - name: Update the apt-cache, if necessary
      apt:
        update_cache: true
        cache_valid_time: 86400
      when: ansible_facts['os_family'] == 'Debian'
  roles:
    # - buluma.docker
    - buluma.setuptools
```

Also see a [full explanation and example](https://buluma.github.io/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/defaults/main.yml):

```yaml
---
# What version of the mozilla/syncserver docker image should we
# install?
# https://hub.docker.com/r/mozilla/syncserver
mozilla_syncserver_docker_version: latest

# A list of additional volumes to mount into the docker container.  This is
# useful for things like SSL certificates and custom css/image assets.
mozilla_syncserver_additional_volumes: []
# - "/some/directory:/some/mount:ro"
# - "/some/file.yml:/some/mount/file.yml:ro"

mozilla_syncserver_port: "5000"

# A key/value set of environment variables and their values, which will be
# set on the docker container.
mozilla_syncserver_environment_variables:
  SYNCSERVER_PUBLIC_URL: "http://localhost:{{ mozilla_syncserver_port }}"
  SYNCSERVER_SECRET: "<PUT YOUR SECRET KEY HERE>"
  SYNCSERVER_SQLURI: "sqlite:////data/syncserver.db"
  SYNCSERVER_BATCH_UPLOAD_ENABLED: "true"
  SYNCSERVER_FORCE_WSGI_ENVIRON: "false"
  PORT: "{{ mozilla_syncserver_port }}"

# If set to a string, the created Docker container will attach to a
# pre-existing default Docker network, instead of creating its own.
mozilla_syncserver_network_name: ""

# Labels to put on the application containers
mozilla_syncserver_container_labels: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | Version |
|-------------|--------|--------|
|[buluma.setuptools](https://galaxy.ansible.com/buluma/setuptools)|[![Ansible Molecule](https://github.com/buluma/ansible-role-setuptools/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-setuptools/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-setuptools.svg)](https://github.com/shadowwalker/ansible-role-setuptools)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://buluma.github.io/) for further information.

Here is an overview of related roles:

![dependencies](https://raw.githubusercontent.com/buluma/ansible-role-mozilla_syncserver/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/buluma):

|container|tags|
|---------|----|
|[Ubuntu](https://hub.docker.com/r/buluma/ubuntu)|all|

The minimum version of Ansible required is 2.9, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/buluma/ansible-role-mozilla_syncserver/issues)

## [Changelog](#changelog)

[Role History](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/CHANGELOG.md)

## [License](#license)

[MIT](https://github.com/buluma/ansible-role-mozilla_syncserver/blob/master/LICENSE)

## [Author Information](#author-information)

[Shadow Walker](https://buluma.github.io/)
