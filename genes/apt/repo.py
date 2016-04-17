from genes.apt.get import APTGet
from genes.apt.package import APTPkg
from genes.process import Process


class APTRepo(Process):
    def __init__(self):
        if not APTPkg.is_installed('software-properties-common'):
            apt_get = APTGet()
            apt_get.update()
            apt_get.install('software-properties-common')

    @staticmethod
    def run(*args, **kwargs):
        super(APTRepo, APTRepo).run('add-apt-repository', '-y', *args, **kwargs)

    @staticmethod
    def add_repo(repo_line):
        APTRepo.run(repo_line)

    @staticmethod
    def add_ppa(ppa):
        APTRepo.run('ppa:' + ppa)
