# Genepool2

WIP: flow thoughts

* User downloads standalone executable and runs it -> evolution master
* it asks for run directory
* it asks for gene manifest. URL or file accepted -> brood
* it resolves web access -> evolution master
* it retrieves repos from manifest and repos' manifests' repos until all repos are retrieved -> repos: genepool, retriver -> evolution master
* it installs python and runs each gene -> evolution master


## Gene heirarchy plans

Genes can be imported by the top brood file or by broodfiles within genepools or modules.
Genes will all be placed at the same level within the evolution master's working folder, under genes/ folder.
Since gene dependency will be flattened and could potentially be cyclic or contain conflicting names, the resolution strategy will be as follows:

* Genepools will be fetched via VCS in the order of declaration.
* Order will be bredth-first, top to bottom. This means that the top level has priority over any subsequent level, etc.
* If only one module in a genepool is used, the genepool-level broodfile will still be imported in its entirity, before the module-level brood file.
This should be taken into proper consideration when organizing genes.
* After fetching the VCS roots, the module folders will be copied from the tag/commit version/branch specified into evolution master's working area.
* If a name conflict exists, a warning message will be emitted informing the user of the issue.
* There will be a flag to prevent ignoring these warnings.
I think by default it will attempt to go forward ignoring them.
This strategy may be reversed depending on how heavily i make use of nested dependencies.
