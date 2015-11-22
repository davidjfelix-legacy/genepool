import os
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


def install(*packages):
    # FIXME: refactor lib if_any function to do this logging
    if not any((is_ubuntu(), is_debian())):
        # FIXME: log fail here.
        return
    if packages:
        Popen(['apt-get', '-y', 'install'] + list(packages), env=Config.ENV)
    else:
        # FIXME: need to output failure
        pass


# FIXME: wrap partials with if_any traits
update = partial(Config.ENV_CALL, Config.APT_GET + ['update'])
upgrade = partial(Config.ENV_CALL, Config.APT_GET + ['upgrade'])


def recv_keys(*keys):
    # FIXME: refactor lib if_any function to do this logging
    if not any((is_ubuntu(), is_debian())):
        # FIXME: log fail here.
        return
    if keys:
        Popen(
            ['apt-key', 'adv', '--keyserver',
             'hpk://pgp.mit.edu:80', '--recv-keys'] + list(keys),
            env=Config.ENV)
    else:
        # FIXME: need to output failure
        pass


def add_repo(*line_items):
    # FIXME: refactor lib if_any function to do this logging
    if not any((is_ubuntu(), is_debian())):
        # FIXME: log fail here.
        return
    if line_items:
        # FIXME: this depends on software-properties-common; debian needs this
        Config.ENV_CALL(Config.ADD_REPO + [" ".join(line_items)])
    else:
        # FIXME: need to output failure
        pass


def add_ppa(ppa):
    # FIXME: refactor lib if_any function to do this logging
    if not any((is_ubuntu(), is_debian())):
        # FIXME: log fail here.
        return
    if ppa:
        Config.ENV_CALL(Config.ADD_REPO + [ppa])
    else:
        # FIXME: need to output failure
        pass
