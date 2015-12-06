#!/usr/bin/env python
import asyncio
import grp
import os
import pwd
from typing import Callable, Optional, TypeVar, Tuple, Dict

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


def run():
    return run_as()


async def run_async():
    await run_as_async()


@only_posix()
def run_as():
    pass


@only_posix()
async def run_as_async(*args: Tuple,
                       user: Optional[IntOrStr] = None,
                       group: Optional[IntOrStr] = None,
                       **kwargs: Dict) -> None:
    if isinstance(user, str):
        user_uid = get_uid_from_username(user)
    else:
        user_uid = user

    if isinstance(group, str):
        user_gid = get_gid_from_groupname(group)
    else:
        user_gid = group

    await asyncio.create_subprocess_exec(
        *args,
        preexec_fn=get_demote(user_uid, user_gid),
        **kwargs)
