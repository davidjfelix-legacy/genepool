import subprocess
from genes.apt import get as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('zsh')
    elif is_osx():
        brew.install('zsh')
        # FIXME this is a bad way to do this
        subprocess.call(
            ['echo', '/usr/local/bin/zsh', '>>', '/etc/shells'],
            shell=True
        )
