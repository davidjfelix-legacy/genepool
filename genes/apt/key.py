from genes.process import Process


class APTKey(Process):
    @staticmethod
    def run(*args, **kwargs):
        super(APTKey).run('apt-key', *args, **kwargs)

    @staticmethod
    def recv_keys(key_id, keyserver='hkp://pgp.mit.edu:80'):
        APTKey.run('adv', '--keyserver', keyserver, '--recv-keys', key_id)
