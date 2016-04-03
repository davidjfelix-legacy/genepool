from abc import ABCMeta, abstractmethod


class Package(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def configure(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def install(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def uninstall(*args, **kwargs):
        raise NotImplementedError
