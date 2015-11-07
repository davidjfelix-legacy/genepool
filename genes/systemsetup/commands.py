import subprocess
from genes.mac.traits import only_osx


@only_osx
def systemsetup(*args):
    subprocess.call(['systemsetup'] + list(args))
