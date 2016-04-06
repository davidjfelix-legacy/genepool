from genes.apt.get import APTGet
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt_get = APTGet()
        apt_get.update()
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
        apt_get.install(*packages)

    else:
        pass
