#!/usr/bin/env python
import asyncio
import grp
import os
import pwd
from typing import Callable, Optional, TypeVar, Tuple, Dict

from subprocess import Popen

from genes.posix.traits import only_posix

IntOrStr = TypeVar("IntOrStr", int, str)


@only_posix()
def get_demote(user_uid: Optional[int] = None,
               user_gid: Optional[int] = None) -> Callable[[], None]:
    def demote() -> None:
        os.setuid(user_uid)
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
def run():
    return run_as()


@only_posix()
async def run_async():
    await run_as_async()


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
