from typing import Callable, Optional
from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main(config: Optional[Callable[[], None]] = None):
    # Install nginx
    if is_ubuntu() or is_debian():
        apt.update()
        apt.install('nginx')
    elif is_osx():
        brew.update()
        brew.install('nginx')
    else:
        pass

    # Then configure it
    if config is not None:
        config()
