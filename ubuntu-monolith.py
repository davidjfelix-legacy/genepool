#!/usr/bin/env python
from __future__ import print_function
import subprocess
import os
import platform


class Gene(object):
    def __init__(self):
        self.count = 0
        self.can_splice = False
        super(self.__class__, self).__init__()

    def __enter__(self):
        self.count += 1
        self.sequence()
        # FIXME: Log this

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        if exc_type and exc_val and exc_tb:
            print("Ran into an exception")
        self.count -= 1
        # FIXME: Log this

    def sequence(self):
        # intentionally blank for mixins
        pass

    def splice(self):
        # intentionally blank for mixins
        pass


class UbuntuSplicer(Gene):
    def sequence(self):
        super(self.__class__, self).sequence()
        self.can_splice = self.can_splice or self.is_ubuntu()

    @staticmethod
    def is_ubuntu():
        return platform.linux_distribution()[0] == 'Ubuntu'


class Apt(Gene, UbuntuSplicer):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.packages = []
        self.repos = []
        self.should_upgrade = False  # Don't upgrade unless you have to
        self.should_update = True

    def splice(self):
        if self.can_splice:
            env = os.environ.copy()
            env['DEBIAN_FRONTEND'] = "noninteractive"
            if self.should_update:
                subprocess.call(['sudo', '-E', 'apt-get', 'update'], env=env)
            if self.should_upgrade:
                subprocess.call(['sudo', '-E', 'apt-get', 'upgrade'], env=env)
            if self.packages:
                subprocess.call(['sudo', '-E', 'apt-get', '-y', 'install'] + packages, env=env)

    def install(self, pkg=None, pkgs=None):
        if pkg and pkgs:
            # TODO/FIXME: decide if this should be an exception, log it
            raise ValueError("Can't define both package and packages")
        elif pkg:
            self.packages.append(pkg)
        elif pkg:
            self.packages += pkg
        else:
            pass  # FIXME: This fail case should be logged

    def update(self):
        # TODO: figure out what to do with this design wise.
        # People really SHOULD update, but how do I accomodate?
        pass

    def upgrade(self):
        self.should_upgrade = True


def brew_install(pkgs=None, cask_pkgs=None):
    subprocess.call(['brew', 'update'])
    if pkgs:
        subprocess.call(['brew', 'install'] + pkgs)
    if cask_pkgs:
        subprocess.call(['brew', 'cask', 'install'] + cask_pkgs)


def brew_cask_install(pkgs):
    brew_install(cask_pkgs=pkgs)


packages = """
- aria2
- atop
- byobu
- curl
- elinks
- emacs
- httpie
- iftop
- iptraf
- iptraf-ng
- ipcalc
- jq
- less
- links
- links2
- lynx
- most
- netcat
- nethogs
- netpipes
- nmap
- rsync
- rsyncrypto
- rtorrent
- screen
- siege
- socat
- squid3
- tmux
- vim
- vim-gtk
- wget
- ack-grep
- ant
- atop
- bastet
- binclock
- boxes
- bsdgames
- build-essential
- byobu
- bzr
- bzr-git
- calcurse
- cloc
- cowsay
- dict
- dstat
- dtach
- duplicity
- emacs
- figlet
- findutils
- fortune
- gcc
- gdb
- gist
- glances
- golang
- gradle
- greed
- htop
- irssi
- jq
- ledger
- less
- lua5.2
- maven
- maven2
- mc
- mdm
- mercurial
- mercurial-git
- moon-buggy
- mosh
- most
- mtr
- multitail
- nethack-console
- nethogs
- netpipes
- ninvaders
- octave
- parallel
- python-software-properties
- qemu
- qemu-kvm
- qalc
- r-base
- ranger
- rbenv
- remind
- ruby
- screen
- siege
- silversearcher-ag
- sl
- slashem
- socat
- squid3
- steghide
- stegsnow
- subversion
- sudo
- sysstat
- task
- toilet
- tpp
- tmux
- tsung
- ttyrec
- vifm
- vim
- vim-gtk
- weechat
- wyrd
- zsh""".split("\n- ")[1:]


def main(packages):
    global apt
    with apt:
        apt.update()
        apt.upgrade()
        apt.install(packages)



if __name__ == "__main__":
    apt = Apt()
    main(packages)
    apt.splice()
