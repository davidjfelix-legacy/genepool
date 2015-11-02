import subprocess
from genes.apt import get as apt


def test_install_package(monkeypatch):
    """Test calling apt.install with one package
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    def mocked_subprocess_call(*args, **kwargs):
        cmd = " ".join(args[0])
        assert(cmd == 'sudo -E apt-get -y install test')
        env = kwargs.get('env', None)
        assert(env is not None)
        assert(env.get('DEBIAN_FRONTEND', None) == 'noninteractive')
        return 0
    
    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    apt.install("test")


def test_install_packages(monkeypatch):
    """Test calling apt install with multiple packages
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    def mocked_subprocess_call(*args, **kwargs):
        cmd = " ".join(args[0])
        assert(cmd == 'sudo -E apt-get -y install test1 test2')
        env = kwargs.get('env', None)
        assert(env is not None)
        assert(env.get('DEBIAN_FRONTEND', None) == 'noninteractive')
        return 0

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    apt.install("test1", "test2")


def test_install_nothing(monkeypatch):
    """Test calling apt install with no packages (failure)
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    def mocked_subprocess_call(*args, **kwargs):
        # This should never be called
        assert not args and not kwargs
        assert False

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    apt.install()
