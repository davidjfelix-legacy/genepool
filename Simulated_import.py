#!/usr/bin/env python
# We're going to simulate how evolution_master should import things

from importlib import import_module

genes = ["docker"]

for gene in genes:
    mod = import_module("genes." + gene)
    mod.main()

# etc...
