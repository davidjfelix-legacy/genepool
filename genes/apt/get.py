import os
from subprocess import call
from functools import partial


#TODO: stop using sudo or ensure it exists
#TODOE: specify user to run as
#TODO: utilize functools partial to handle some of the above functionality
class Config:
    APT_GET = ['sudo', '-E', 'apt-get']
    ADD_REPO = ['sudo', '-E', 'add-apt-repository', '-y']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"
    ENV_CALL = partial(call, env=ENV)
    #TODO: Split me out to key
    RECV_KEY = ['sudo', '-E', 'apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80', '--recv-keys']

def install(*packages):
    if packages:
        Config.ENV_CALL(Config.APT_GET + ['install'] + list(packages))
    else:
        #FIXME: need to output failure
        pass
    

update = partial(Config.ENV_CALL, Config.APT_GET + ['update'])
upgrade = partial(Config.ENV_CALL, Config.APT_GET + ['upgrade'])

def recv_keys(*keys):
    if keys:
        Config.ENV_CALL(Config.RECV_KEY + list(keys))
    else:
        #FIXME: need to output failure
        pass
    
def add_repo(filename, *line_items):
    if filename and line_items:
        #FIXME: this depends on software-properties-common; debian needs this
        Config.ENV_CALL(Config.ADD_REPO + ['"' + " ".join(line_items) + '"'])
    else:
        #FIXME: need to output failure
        pass
