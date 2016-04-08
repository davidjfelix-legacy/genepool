from genes.apt.get import APTGet
from genes.apt.package import APTPkg
from genes.process import Process


class APTKey(Process):
    def __init__(self):
        if not all((APTPkg.is_installed('apt-transport-https'), APTPkg.is_installed('ca-certificates'))):
            apt_get = APTGet()
            apt_get.update()
            apt_get.install('apt-transport-https', 'ca-certificates')

    @staticmethod
    def run(*args, **kwargs):
        return super(APTKey, APTKey).run('apt-key', *args, **kwargs)

    @staticmethod
    def recv_keys(key_id, keyserver='hkp://pgp.mit.edu:80'):
        APTKey.run('adv', '--keyserver', keyserver, '--recv-keys', key_id)
