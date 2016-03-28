#!/usr/bin/env python
import asyncio
import grp
import os
import pwd
from subprocess import Popen
from typing import Callable, Optional, TypeVar, Tuple, Dict

from genes.posix.traits import only_posix

IntOrStr = TypeVar("IntOrStr", int, str)


@only_posix()
def get_env_run(my_env: Dict):
    def env_run(*args: Tuple, **kwargs: Dict) -> Callable:
        return run(*args, env=my_env, **kwargs)

    return env_run


@only_posix()
def get_env_run_as(my_env):
    def env_run_as(*args, user, group, **kwargs):
        return run_as(*args, user, group, env=my_env, **kwargs)

    return env_run_as


@only_posix()
def get_demote(user_uid: Optional[int] = None,
               user_gid: Optional[int] = None) -> Callable[[], None]:
    def demote() -> None:
        if user_uid is not None:
            os.setuid(user_uid)
        if user_gid is not None:
            os.setgid(user_gid)

    return demote


@only_posix()
def get_uid_from_username(username: str) -> Optional[int]:
    try:
        return pwd.getpwnam(username).pw_uid
    except KeyError:
        return None


@only_posix()
def get_gid_from_groupname(groupname: str) -> Optional[int]:
    try:
        return grp.getgrnam(groupname).gr_gid
    except KeyError:
        return None


@only_posix()
def run(*args: Tuple, **kwargs: Dict):
    return run_as(*args, **kwargs)


@only_posix()
async def run_async(*args: Tuple, **kwargs: Dict):
    await run_as_async(*args, **kwargs)


@only_posix()
def run_as(*args: Tuple,
           user: Optional[IntOrStr] = None,
           group: Optional[IntOrStr] = None,
           **kwargs: Dict) -> None:
    user_uid = get_uid_from_username(user) if isinstance(user, str) else user
    user_gid = get_gid_from_groupname(group) if \
        isinstance(group, str) else group

    Popen(*args, preexec_fn=get_demote(user_uid, user_gid), **kwargs).wait()


@only_posix()
async def run_as_async(*args: Tuple,
                       user: Optional[IntOrStr] = None,
                       group: Optional[IntOrStr] = None,
                       **kwargs: Dict) -> None:
    user_uid = get_uid_from_username(user) if isinstance(user, str) else user
    user_gid = get_gid_from_groupname(group) if \
        isinstance(group, str) else group

    await asyncio.create_subprocess_exec(
            *args,
            preexec_fn=get_demote(user_uid, user_gid),
            **kwargs)
