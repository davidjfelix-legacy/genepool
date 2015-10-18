#!/usr/bin/env python
from __future__ import print_function
from genes import apt

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
    apt.update()
    apt.upgrade()
    apt.install(*packages)


if __name__ == "__main__":
    main(packages)
