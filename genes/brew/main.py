import subprocess
from genes.curl.commands import download
from genes.mac.traits import only_osx


@only_osx
def main():
    download(
        'https://raw.githubusercontent.com/Homebrew/install/master/install',
        '/tmp/brew_install'
    )
    subprocess.call(['ruby', '-e', '/tmp/brew_install'])
