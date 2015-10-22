from genes import brew
from genes.debian import is_debian
from genes.mac import is_osx
from genes.ubuntu import is_ubuntu
from genes.curl import download

def main():
    if is_debian() or is_ubuntu():
        download("https://download.jetbrains.com/idea/ideaIU-14.1.5.tar.gz", "/tmp/ideas.tar.gz")
        #FIXME: get the file from tmp, untar it to opt. this is a PITA
    if is_osx():
        brew.cask_install('intellij-idea')

    else:
        pass
