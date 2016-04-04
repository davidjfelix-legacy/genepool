from genes.process import Process


class AptKey(Process):
    @staticmethod
    def run(cmd, **kwargs):
        super(AptKey).run(['apt-key'] + cmd)

    @staticmethod
    def recv_keys(key_id, keyserver='hkp://pgp.mit.edu:80'):
        AptKey.run(['adv', '--keyserver', keyserver, '--recv-keys', key_id])
