from genes.apt.get import APTGet
from genes.apt.package import APTPkg
from genes.lib.exceptions import OSNotSupportedError
from genes.os.traits import get_os
from genes.package import Package


class CurlPkg(Package):
    def __init__(self, apt_get=None, os_name=None):
        self.os_name = os_name if os_name else get_os()
        self.apt_get = apt_get if apt_get else APTGet()

        if self.os_name == 'debian' or self.os_name == 'ubuntu':
            self.apt_get.update()

    def uninstall(self, *args, **kwargs):
        os_name = get_os()
        if os_name == 'debian' or os_name == 'ubuntu':
            self.apt_get.remove('curl')
        else:
            raise OSNotSupportedError('Operating system not supported by CurlPkg')

    def configure(self, *args, **kwargs):
        pass

    def is_installed(self):
        if self.os_name == 'debian' or self.os_name == 'ubuntu':
            return APTPkg.is_installed('curl')
        else:
            return False

    def install(self, *args, **kwargs):
        os_name = get_os()
        if os_name == 'debian' or os_name == 'ubuntu':
            self.apt_get.install('curl')
        else:
            raise OSNotSupportedError('Operating system not supported by CurlPkg')
