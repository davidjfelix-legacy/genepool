import os
from genes.lib.traits import if_any
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from subprocess import call, Popen
from functools import partial


# TODO: utilize functools partial to handle some of the above functionality
class Config:
    APT_GET = ['apt-get', '-y']
    ADD_REPO = ['add-apt-repository', '-y']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"
    ENV_CALL = partial(call, env=ENV)
    # TODO: Split me out to key
    RECV_KEY = ['apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80', '--recv-keys']


def install(*packages):
    # FIXME: refactor lib if_any function to do this logging
    if not any((is_ubuntu(), is_debian())):
        # FIXME: log fail here.
        return
    if packages:
        Popen(['apt-get', '-y', 'install'] + list(packages), env=Config.ENV)
        #Config.ENV_CALL(Config.APT_GET + ['install'] + list(packages))
    else:
        # FIXME: need to output failure
        pass


# FIXME: wrap partials with if_any traits
update = partial(Config.ENV_CALL, Config.APT_GET + ['update'])
upgrade = partial(Config.ENV_CALL, Config.APT_GET + ['upgrade'])


@if_any(is_debian, is_ubuntu)
def recv_keys(*keys):
    if keys:
        Config.ENV_CALL(Config.RECV_KEY + list(keys))
    else:
        # FIXME: need to output failure
        pass


@if_any(is_debian, is_ubuntu)
def add_repo(*line_items):
    if line_items:
        # FIXME: this depends on software-properties-common; debian needs this
        Config.ENV_CALL(Config.ADD_REPO + [" ".join(line_items)])
    else:
        # FIXME: need to output failure
        pass


@if_any(is_debian, is_ubuntu)
def add_ppa(ppa):
    if ppa:
        Config.ENV_CALL(Config.ADD_REPO + [ppa])
    else:
        # FIXME: need to output failure
        pass
