import os
import subprocess

def install(*packages):
    if packages:
        env = os.environ.copy()
        env['DEBIAN_FRONTEND'] = "noninteractive"
        subprocess.call(['sudo', '-E', 'apt-get', '-y', 'install'] + list(packages), env=env)
    else:
        #FIXME: need to output failure
        pass
    
def update():
    env = os.environ.copy()
    env['DEBIAN_FRONTEND'] = "noninteractive"
    subprocess.call(['sudo', '-E', 'apt-get', 'update'], env=env)
    
def upgrade():
    env = os.environ.copy()
    env['DEBIAN_FRONTEND'] = "noninteractive"
    subprocess.call(['sudo', '-E', 'apt-get', 'upgrade'], env=env)
