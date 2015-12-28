# genepool

[![Brood](http://img.shields.io/badge/brood-Hatchery-735145.svg?style=flat-square)](https://github.com/hatchery)
[![Travis](https://img.shields.io/travis/hatchery/genepool.svg?style=flat-square)](https://travis-ci.org/hatchery/genepool)
[![License](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://github.com/hatchery/genepool/blob/master/LICENSE.md)
[![Github Issues](https://img.shields.io/github/issues/hatchery/genepool.svg?style=flat-square)](https://github.com/hatchery/genepool/issues)
[![Github Release](https://img.shields.io/github/release/hatchery/genepool.svg?style=flat-square)](https://github.com/hatchery/genepool/releases)


WIP: Thoughts on how hatchery flow will work

* The user navigates to evolution master's page and downloads the standalone executable.
* The user runs the executable.
* The executable escalates to local admin.
* The executable asks for a temp director
* The executable asks for a top level broodfile. path or URL acceptable
* The web address is resolved (proxy)
* The executable retrieves repos from the broodfile. These repos are genepools.
* Recursively get the repos from each level's dependencies
* The executable installs a bundled python environment and runs the broodfile runner and top level genes.

## User strategy

On Linux/BSD it's pretty common to have root-equivalent access (root or sudo) to modify the local system and install software.
However, on OSX and Windows things get a little bit fuzzier.
On OSX, using homebrew has the strategy of escalating to root equivalent but only to chmod an area of user-level directories in `/usr/local`, not to install software itself.
To handle this "run as admin user, not root" design, genepool will be designed to run as root-equivalent and will de-escalate itself to a user of its choice.
For hatchery/genepool/genes/adminuser, we'll use the name `splicer`.
If this is your username, you can configure the gene to use a different name.

* For brew, the `/usr/local` directory will be altered to run with g+w set so that anyone in the group can use it.
* Windows strategy is still pending
* Modules should be written in a way that has access to root, users being provisioned by a gene or utilize splicer and group level access for splicer's peers.


## Sample use

From this directory, you can use genes. Typical use is as follows:

```python
from genes.docker import main as _docker

_docker()
```



## Gene heirarchy plans

Genes can be imported by the top brood file or by broodfiles within genepools or modules.
Genes will all be placed at the same level within the evolution master's working folder, under genes/ folder.
Since gene dependency will be flattened and could potentially be cyclic or contain conflicting names, the resolution strategy will be as follows:

* Genepools will be fetched via VCS in the order of declaration.
* Order will be bredth-first, top to bottom, in the order declared within the level broodfile. This means that the top level has priority over any subsequent level, etc.
* If only one module in a genepool is used, the genepool-level broodfile will still be imported in its entirity, before the module-level brood file.

Pseudocode algorithm:
```
clear all genes from genes
sort broodfiles level-based, top to bottom, a-z gene within level
for broodfile in broodfiles:
  # genepools are declared in order within the broodfile
  for genepool in broodfile:
    if genepool.vcs does not exist in vcs_store:
      clone genepool.vcs
    for gene in genepool:
      if directory by gene.name does not exist in genes:
        pull from genepool.vcs # to ensure vcs is up to date
        checkout genepool.vcs genepool.tag/branch/commit
        move directory by gene.name to genes
      else:
        emit warning/error about duplicate genes
```
This should be taken into proper consideration when organizing genes.
* After fetching the VCS roots, the module folders will be copied from the tag/commit version/branch specified into evolution master's working area.
* If a name conflict exists, a warning message will be emitted informing the user of the issue.
* There will be a flag to prevent ignoring these warnings.
I think by default it will attempt to go forward ignoring them.
This strategy may be reversed depending on how heavily i make use of nested dependencies.


# The way it works

* Everything is a gene; things that run things are genes, things that install things are genes
* Genes that get used one time are typically top level genes, you declare them in your top level brood file
* Genes that are used by genes to accomplish their goal (installing go gene requires homebrew gene) frequently are called by 'n' number of genes.
* These genes are declared as dependencies and are not typically run unless called upon by other genes or declared at top level.
* Homebrew would be a gene that makes sense to declare at top level, because you install it.
* Apt would be a gene that does not make sense to declare at top level (typically) because it's bundled with Debian.
