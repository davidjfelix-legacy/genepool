#!/usr/bin/env python
# This file is intentionally blank
# It is used by python to create a module structure
from invoke import Collection

from genes.docker.package import DockerPkg

docker = DockerPkg()
ns = Collection()
ns.add_collection(docker.collection)
