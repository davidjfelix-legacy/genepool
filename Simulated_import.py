#!/usr/bin/env python
# We're going to simulate how evolution_master should import things

from importlib import import_module

genes = ["docker", "java", "web_cli_tools", "intellij"]

for gene in genes:
    mod = import_module("genes." + gene)
    mod.main.main()

# etc...
