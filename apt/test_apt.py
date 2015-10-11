import subprocess
import apt

def test_install_package(monkeypatch):
    def mocked_subprocess_call(*args, **kwargs):
        assert(args[0] == ['sudo', '-E', 'apt-get', '-y', 'install', 'test'])
        return 0
    
    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    sut = apt.install("test")


def test_install_packages(monkeypatch):
    def mocked_subprocess_call(*args, **kwargs):
        assert(args[0] == ['sudo', '-E', 'apt-get', '-y', 'install', 'test1', 'test2'])
        return 0

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    sut = apt.install("test1", "test2")

def test_install_nothing(monkeypatch):
    def mocked_subprocess_call(*args, **kwargs):
        # This should never be called
        assert(False)
        return 1

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    sut = apt.install()
