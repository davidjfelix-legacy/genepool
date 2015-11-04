from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu
from genes.curl.commands import download
from genes.tar.commands import untar
from genes.directory import DirectoryBuilder


def main():
    if is_debian() or is_ubuntu():
        download(
            "https://download.jetbrains.com/idea/ideaIU-15.0.tar.gz",
            "/tmp/ideas.tar.gz"
        )
        DirectoryBuilder('/opt/intellij-ideas')\
            .set_mode('755')\
            .set_group('root')\
            .set_user('root')\
            .build()
        untar('/tmp/ideas.tar.gz', '/opt/intellij-ideas')
    if is_osx():
        brew.update()
        brew.cask_install('intellij-idea')
    else:
        pass
