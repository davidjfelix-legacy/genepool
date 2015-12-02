import subprocess

from genes.posix.traits import is_posix


# FIXME: use tar module
# FIXME: I'm sure I don't have permissions to this destination
def untar(source, destination):
    # FIXME: make this silent
    if is_posix():
        subprocess.call(['tar', '-xvzf', source, '-C', destination])
    else:
        # FIXME: handle windows
        pass
