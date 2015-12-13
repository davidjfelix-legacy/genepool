from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        # FIXME: debian needs ppa software
        apt.add_ppa('neovim-ppa/unstable')
        apt.update()
        apt.install('neovim')
    elif is_osx():
        brew.update()
        # FIXME: Beetlejuice Beetlejuice Beetlejuice
        brew.cask_install('neovim/neovim/neovim')
    else:
        # FIXME: print failure, handle windows
        pass
