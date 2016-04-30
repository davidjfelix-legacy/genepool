from genes.group import Group
from genes.os.traits import get_os
from genes.package import Package
from genes.user import User


class AdminUser(Package):
    def __init__(self, *args, os_name=get_os(), username='splicer', **kwargs):
        self.os_name = os_name
        self.username = username
        self.group = Group()
        self.user = User(username=self.username, os_name=self.os_name)

    def uninstall(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        pass

    def is_installed(self, *args, **kwargs):
        pass

    def install(self, *args, **kwargs):
        if self.os_name in ('debian', 'ubuntu'):
            self.group.install()
            self.user.groups = ('sudo',)
        if self.os_name == 'osx':
            self.group.install()
            self.user.groups = ('admin',)

        self.user.install()
