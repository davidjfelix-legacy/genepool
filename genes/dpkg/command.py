from genes.process import Process


class Dpkg(Process):
    @staticmethod
    def run(*args, **kwargs):
        return super(Dpkg, Dpkg).run('dpkg', *args, **kwargs)

    @staticmethod
    def is_package_installed(package):
        response_code = Dpkg.run('-s', package)
        return response_code == 0

