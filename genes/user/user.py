from genes.dscl.dscl import DSCL
from genes.gnu_coreutils.commands import useradd
from genes.os.traits import get_os
from genes.package import Package


class User(Package):
    def is_installed(self, *args, **kwargs):
        pass

    def __init__(self, *args, os_name=get_os(), username=None, groups=(), **kwargs):
        self.username = username
        self.groups = groups
        self.os_name = os_name

        if self.os_name == 'osx':
            self.dscl = DSCL()
        elif self.os_name in ('debian', 'ubuntu'):
            pass

    def uninstall(self, *args, **kwargs):
        pass

    def configure(self, username, *args, groups=(), **kwargs):
        pass

    @property
    def is_configured(self):
        return self.username is not None

    def install(self, *args, **kwargs):
        if not self.is_configured:
            # TODO: Raise exception somehow and exit flow
            pass

        if self.os_name == 'osx':
            if not self.is_installed():
                self.dscl.create('/Users/' + self.username)
        if self.os_name in ('debian', 'ubuntu'):
            useradd()
