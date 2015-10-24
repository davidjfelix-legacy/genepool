import subprocess
from genes.curl import download
from genes.mac import only_osx


@only_osx
def main():
    download(
        'https://raw.githubusercontent.com/Homebrew/install/master/install',
        '/tmp/brew_install'
    )
    subprocess.call(['ruby', '-e', '/tmp/brew_install'])
