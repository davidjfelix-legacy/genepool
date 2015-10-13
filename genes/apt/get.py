import os
from subprocess import call
from functools import partial


#TODO: stop using sudo or ensure it exists
#TODOE: specify user to run as
#TODO: utilize functools partial to handle some of the above functionality
class Confg:
    APT_GET = ['sudo', '-E', 'apt-get']
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"
    ENV_CALL = partial(call, env=ENV)

def install(*packages):
    if packages:
        Config.ENV_CALL(Config.APT_GET + ['install'] + list(packages))
    else:
        #FIXME: need to output failure
        pass
    

update = partial(Config.ENV_CALL, APT_GET + ['update'])
upgrade = partial(Config.ENV_CALL, APT_GET + ['upgrade'])
