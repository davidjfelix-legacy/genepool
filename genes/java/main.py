from typing import Callable, Dict

from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debconf import commands as debconf
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main(configure: Callable[[], Dict]):
    if is_debian() or is_ubuntu():
        config = configure()
        if config['is_oracle']:
            # FIXME: debian needs ppa software
            apt.add_ppa('webupd8team/java')
            apt.update()
            debconf.set_selections(config['version'] + '-installer',
                                   'shared/accepted-oracle-license-v1-1',
                                   'select', 'true')
            apt.install(config['version'] + '-installer')
        else:
            apt.update()
            apt.install(config['version'])

    elif is_osx():
        brew.update()
        brew.cask_install('java')
    else:
        # FIXME: print failure, handle windows
        pass
