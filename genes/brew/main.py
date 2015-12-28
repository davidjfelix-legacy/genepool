import os

from genes.curl.commands import download
from genes.mac.traits import only_osx
from genes.process.commands import get_env_run_as, run
from .commands import install


class Config(object):
    # FIXME: this structure should not exist
    ENV = os.environ.copy()
    USER = 'splicer'
    GROUP = 'admin'


env_run_as = get_env_run_as(Config.ENV)


@only_osx()
def main():
    # FIXME: this download should go to a mktmp directory
    download(
        'https://raw.githubusercontent.com/Homebrew/install/master/install',
        '/tmp/brew_install'
    )
    env_run_as(['ruby', '-e', '/tmp/brew_install'], Config.USER, Config.GROUP)
    install('caskroom/cask/brew-cask')
    # FIXME: extract this to a chmod command
    run('chmod -R g+w /usr/local')
