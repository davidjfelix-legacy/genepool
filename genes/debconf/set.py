import os
from subprocess import Popen, PIPE
from genes.lib.traits import if_any
from genes.ubuntu.traits import is_ubuntu
from genes.debian.traits import is_debian


# TODO: stop using sudo or ensure it exists
# TODO: specify user to run as
# TODO: utilize functools partial to handle some of the above functionality
class Config:
    SET_SELECTIONS = ['debconf-set-selections']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


@if_any(is_debian, is_ubuntu)
def set_selections(*selections):
    if selections:
        debconf = Popen(Config.SET_SELECTIONS, env=Config.ENV, stdin=PIPE)
        debconf.communicate(input=" ".join(selections))
        # FIXME: capture errors above, report them
    else:
        # FIXME: add error
        pass
