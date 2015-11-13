from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debconf import set as debconf
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from genes.mac.traits import is_osx


def main(config):
    if is_debian() or is_ubuntu():
        # FIXME: debian needs ppa software
        apt.add_ppa('ppa:neovim-ppa/unstable')
        apt.update()
        debconf.set_selections(config.version + '-installer',
                               'shared/accepted-oracle-license-v1-1',
                               'select', 'true')
        apt.install('neovim')

    elif is_osx():
        brew.update()
        # FIXME: Beetlejuice Beetlejuice Beetlejuice
        brew.cask_install('neovim/neovim/neovim')
    else:
        # FIXME: print failure, handle windows
        pass