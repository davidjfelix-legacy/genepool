from genes import apt, brew
from genes.debian import is_debian
from genes.mac import is_osx
from genes.ubuntu import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        packages = (
            "aria2",
            "atop",
            "byobu",
            "curl",
            "elinks",
            "emacs",
            "hatop",
            "htop",
            "httpie",
            "iftop",
            "iptraf",
            "iptraf-ng",
            "ipcalc",
            "jq",
            "less",
            "links",
            "links2",
            "lynx",
            "most",
            "netcat",
            "nethogs",
            "netpipes",
            "nmap",
            "rsync",
            "rsyncrypto",
            "rtorrent",
            "screen",
            "siege",
            "socat",
            "squid3",
            "tmux",
            "vim",
            "vim-gtk",
            "wget"
        )
        apt.install(*packages)

    elif is_osx():
        brew.update()

    else:
        pass
