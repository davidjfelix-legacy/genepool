import os

from genes.alpine.traits import only_alpine
from genes.lib.logging import log_error
from genes.process.commands import get_env_run

env_run = get_env_run(os.environ.copy())


@only_alpine()
def add(*packages) -> None:
    if packages:
        env_run('apk --no-cache add'.split() + list(packages))
    else:
        msg = 'Missing packages argument'
        log_error(msg)
        raise ValueError(msg)


@only_alpine()
def delete(*packages) -> None:
    if packages:
        env_run('apk del'.split() + list(packages))
    else:
        msg = 'Missing packages argument'
        log_error(msg)
        raise ValueError(msg)
