import subprocess

from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def make_default(username=None):
    if username:
        if is_debian() or is_ubuntu():
            subprocess.call(['usermod', '-s', '/usr/bin/zsh', username])
        elif is_osx():
            subprocess.call(['usermod', '-s', '/usr/local/bin/zsh', username])
            # FIXME: if no username, make all users login shell zsh
