from genes.dscl.dscl import DSCL
from genes.gnu_coreutils.commands import groupadd
from genes.os.traits import get_os
from genes.package import Package


class Group(Package):
    def __init__(self, *args, os_name=get_os(), groupname=None, **kwargs):
        self.os_name = os_name
        self.groupname = groupname
        if os_name in ('debian', 'ubuntu'):
            # TODO: get a core utils handler
            pass
        elif os_name == 'osx':
            self.dscl = DSCL()

    def install(self, *args, **kwargs):
        if not self.is_configured:
            # TODO: raise exception somehow
            pass

        if self.os_name == 'osx':
            self.dscl.create('/Groups/' + self.groupname)
        elif self.os_name in ('debian', 'ubuntu'):
            groupadd(self.groupname)

    @property
    def is_configured(self):
        return self.groupname is not None

    def uninstall(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        pass

    def is_installed(self, *args, **kwargs):
        pass
