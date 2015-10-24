import subprocess
from genes import apt, brew
from genes.debian import is_debian
from genes.mac import is_osx
from genes.ubuntu import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('zsh')
    elif is_osx():
        brew.install('zsh')
        # FIXME this is a bad way to do this
        subprocess.call(
            ['sudo', 'echo', '/usr/local/bin/zsh', '>>', '/etc/shells'],
            shell=True
        )
