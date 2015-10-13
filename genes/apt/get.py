import os
import subprocess


#TODO: stop using sudo or ensure it exists
#TODOE: specify user to run as
#TODO: utilize functools partial to handle some of the above functionality

APT_GET = ['sudo', '-E', 'apt-get']
ENV = os.environ.copy()
ENV['DEBIAN_FRONTEND'] = "noninteractive"

def install(*packages):
    global APT_GET, ENV
    if packages:
        subprocess.call(APT_GET + ['install'] + list(packages), env=ENV)
    else:
        #FIXME: need to output failure
        pass
    
def update():
    global APT_GET, ENV
    subprocess.call(APT_GET + ['update'], env=ENV)
    
def upgrade():
    global APT_GET, ENV
    subprocess.call(APT_GET + ['upgrade'], env=ENV)
