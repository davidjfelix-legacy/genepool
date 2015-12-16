import subprocess
from genes.curl.commands import download
from genes.mac.traits import only_osx


@only_osx
def main():
    download(
        'https://raw.githubusercontent.com/Homebrew/install/master/install',
        '/tmp/brew_install'
    )
    # FIXME: install as non-root
    subprocess.call(['ruby', '-e', '/tmp/brew_install'])
    # FIXME: install cask
    # FIXME: recursively claim the /usr/local/bin directory for non-root user
    pass
