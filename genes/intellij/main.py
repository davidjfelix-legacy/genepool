from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu
from genes.curl.commands import download
from genes.tar.commands import untar


def main():
    if is_debian() or is_ubuntu():
        download(
            "https://download.jetbrains.com/idea/ideaIU-14.1.5.tar.gz",
            "/tmp/ideas.tar.gz"
        )
        untar('/tmp/idea.tar.gz', '/opt/')
    if is_osx():
        brew.cask_install('intellij-idea')

    else:
        pass
