#!/usr/bin/env python


class UserBuilder(object):
    def __init__(self, username):
        self.username = username
        self.groups = []
        self.shell = None

    def add_group(self, group):
        self.groups.append(group)
        return self

    def set_groups(self, groups):
        self.groups = groups
        return self

    def set_shell(self, shell):
        self.shell = shell
        return self

    def build(self):
        # FIXME: build user in an idempotent manner
        pass
