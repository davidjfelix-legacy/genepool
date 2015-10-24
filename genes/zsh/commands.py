import subprocess
from genes.debian import is_debian
from genes.ubuntu import is_ubuntu
from genes.mac import is_osx


def make_default(username=None):
    if username:
        if is_debian() or is_ubuntu():
            subprocess.call(['sudo', 'chsh', '-s', '/usr/bin/zsh'])
        elif is_osx():
            subprocess.call(['sudo', 'chsh', '-s', '/usr/local/bin/zsh'])
    # FIXME: if no username, make all users login shell zsh
