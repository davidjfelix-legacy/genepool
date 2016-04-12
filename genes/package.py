from abc import ABCMeta, abstractmethod


class Package(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_installed(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def configure(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def install(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def uninstall(self, *args, **kwargs):
        raise NotImplementedError
