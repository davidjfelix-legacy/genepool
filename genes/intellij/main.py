from genes.brew import commands as brew
from genes.curl.commands import download
from genes.debian.traits import is_debian
from genes import directory
from genes.directory import DirectoryConfig
from genes.mac.traits import is_osx
from genes.tar.commands import untar
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        download(
            "https://download.jetbrains.com/idea/ideaIU-15.0.tar.gz",
            "/tmp/ideas.tar.gz"
        )
        def config_directory()
            return DirectoryConfig(
                path='/opt/intellij-ideas',
                mode='755',
                group='root',
                user='root',
            )
        # FIXME: Need to find a way to handle errors here
        direcotry.main(config_directory)
        untar('/tmp/ideas.tar.gz', '/opt/intellij-ideas')
    if is_osx():
        brew.update()
        brew.cask_install('intellij-idea')
    else:
        pass
