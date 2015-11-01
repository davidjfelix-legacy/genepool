import subprocess
from genes.apt import get as  apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu:
        apt.update()
        apt.install('squid3')
    elif is_osx():
        brew.install('squid')
    else:
        # FIXME windows et al
        pass


def config_file(filename):
    pass


def enable(start=True):
    if start:
        start()
        if is_debian() or is_ubuntu():
            # FIXME: remove subprocess call here... create systemd module
            subprocess.call(['sudo', 'systemctl', 'enable', 'squid3'])
        elif is_osx():
            # FIXME: remove subprocess call here... create launchd module
            subprocess.call(['sudo', 'launchctl', 'load', '-w', '~/Library/LaunchAgents/squid.plist'])


def start():
    # FIXME: hardcoded stuff; windows support
    if is_debian() or is_ubuntu():
        subprocess.call(['sudo', 'systemctl', 'start', 'squid3'])
    elif is_osx():
        subprocess.call(['sudo', 'launchctl', 'start', 'squid'])

