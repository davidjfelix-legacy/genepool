from __future__ import print_function
import genes
import subprocess
from .commands import install
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu


def test_install_package(mocker):
    """Test calling apt.install with one package
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    mocker.patch('genes.apt.commands.Config.ENV_CALL')
    install("test")
    genes.apt.commands.Config.ENV_CALL.assert_not_called()


def test_install_packages(monkeypatch):
    """Test calling apt install with multiple packages
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    # FIXME: this test should fail
    def mocked_subprocess_call(*args, **kwargs):
        cmd = " ".join(args[0])
        assert(cmd == 'sudo -E apt-get -y install test1 test2')
        env = kwargs.get('env', None)
        assert(env is not None)
        assert(env.get('DEBIAN_FRONTEND', None) == 'noninteractive')
        return 0

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    install("test1", "test2")


def test_install_nothing(monkeypatch):
    """Test calling apt install with no packages (failure)
    :param monkeypatch: This is the py.test monkeypatching for mock.
    """
    def mocked_subprocess_call(*args, **kwargs):
        # This should never be called
        assert not args and not kwargs
        assert False

    monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
    install()
