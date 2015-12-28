import os
from subprocess import Popen, PIPE

from genes.debian.traits import is_debian
from genes.lib.logging import log_error
from genes.lib.traits import if_any_funcs
from genes.ubuntu.traits import is_ubuntu


class Config(object):
    SET_SELECTIONS = ['debconf-set-selections']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


@if_any_funcs(is_debian, is_ubuntu)
def set_selections(*selections):
    if selections:
        debconf = Popen(Config.SET_SELECTIONS, env=Config.ENV, stdin=PIPE)
        debconf.communicate(input=" ".join(selections))
        debconf.wait()
    else:
        msg = "Missing selections argument"
        log_error(msg)
        raise ValueError(msg)
