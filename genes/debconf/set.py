import os
from functools import partial
from subprocess import Popen, PIPE
from genes.lib.traits import run_if_any_funcs
from genes.ubuntu.traits import is_ubuntu
from genes.debian.traits import is_debian


# TODO: stop using sudo or ensure it exists
# TODO: specify user to run as
# TODO: utilize functools partial to handle some of the above functionality
class Config:
    SET_SELECTIONS = ['debconf-set-selections']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


def set_selections(*selections):
    if selections:
        run_if_deb_or_ubu = partial(run_if_any_funcs, [is_ubuntu, is_debian])
        set_sel_func = partial(set_selections, *selections)
        run_if_deb_or_ubu(set_sel_func)
    else:
        # FIXME: log
        pass


def _set_selections(*selections):
    debconf = Popen(Config.SET_SELECTIONS, env=Config.ENV, stdin=PIPE)
    debconf.communicate(input=" ".join(selections))
    debcong.wait()

