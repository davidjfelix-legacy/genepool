import os
from subprocess import Popen, PIPE


# TODO: stop using sudo or ensure it exists
# TODO: specify user to run as
# TODO: utilize functools partial to handle some of the above functionality
class Config:
    SET_SELECTIONS = ['sudo', '-E', 'debconf-set-selections']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


def set_selections(*selections):
    if selections:
        debconf = Popen(Config.SET_SELECTIONS, env=Config.ENV, stdin=PIPE)
        debconf.communicate(input=" ".join(selections))
        # FIXME: capture errors above, report them
    else:
        # FIXME: add error
        pass
