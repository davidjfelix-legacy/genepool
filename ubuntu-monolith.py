#!/usr/bin/env python

import subprocess
import os


from __future__ import print_function

class apt_gene(object):
    def __init__(self):
        self.count = 0
        self.packages = []
        self.repos = []
        self.should_update = None #TODO: Consider optional boolean

    def __enter__(self):
        self.count += 1
        #FIXME: Log this

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.count -= 1
        #FIXME: Log this

    def install(self, package=None, packages=None):
        if package and packages:
            #TODO/FIXME: decide if this should be an exception, log it
            raise ValueError("Can't define both package and packages")
        elif package:
            self.packages.append(package)
        elif packages:
            self.packages += packages
        else:
            pass #FIXME: This fail case should be logged

    def update(self):
        self.should_update = True



apt = apt_gene()

def apt_install(packages):
    env = os.environ.copy()
    env[DEBIAN_FRONTEND] = "noninteractive"
    subprocess.call(['sudo', '-E', 'apt-get', 'update'], env=env)
    subprocess.call(['sudo', '-E', 'apt-get', '-y', 'install'] + packages, env=env)

def brew_install(packages=None, cask_packages=None):
    subprocess.call(['brew', 'update'])
    if packages:
        subprocess.call(['brew', 'install'] + packages)
    if cask_packages:
        subprocess.call(['brew', 'cask', 'install'] + cask_packages)

def brew_cask_install(packages):
    brew_install(cask_packages=packages)
  
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
- zsh""".split("\n- ")

apt_install(packages)

def main(packages):
    with apt:
        apt.update()
        apt.install(packages)
