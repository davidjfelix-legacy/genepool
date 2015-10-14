import os
from subprocess import call
from functools import partial

#TODO: stop using sudo or ensure it exists
#TODOE: specify user to run as
#TODO: utilize functools partial to handle some of the above functionality
class Config:
    SET_SELECTIONS = ['sudo', '-E', 'debconf-set-selections']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"
    ENV_CALL = partial(call, env=ENV)
    
def set_selections(*selections):
    if selections:
        Config.ENV_CALL(['echo'] + list(selections) + ['|'] + Config.SET_SELECTIONS)
    else:
        #FIXME: add error
        pass
