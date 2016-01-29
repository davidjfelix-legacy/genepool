from genes.process.commands import get_env_run
from .traits import only_posix

run = get_env_run()


@only_posix()
def chmod(*args):
    # FIXME: this is ugly, name the args
    run(['chmod'] + list(*args))
