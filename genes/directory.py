#!/usr/bin/env python
from genes.gnu_coreutils.commands import chgrp, chown, mkdir
from genes.posix.traits import is_posix


class DirectoryBuilder(object):
    def __init__(self, path):
        self.path = path
        self.mode = '777'
        self.group = 'root'
        self.user = 'root'

    def set_mode(self, mode):
        self.mode = mode
        return self

    def set_user(self, user):
        self.user = user
        return self

    def set_group(self, group):
        self.group = group
        return self

    def build(self):
        if is_posix():
            mkdir(self.path, mode=self.mode)
            chown(self.path, self.user)
            chgrp(self.path, self.group)
        else:
            pass
