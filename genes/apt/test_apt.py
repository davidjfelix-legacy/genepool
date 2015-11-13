#!/usr/bin/env python
from six.moves import reload_module
import mock
import genes
from .commands import install


# Set up a non-apt system first
# FIXME: move these to a setup method
mock_is_debian = mock.patch('genes.debian.traits.is_debian', lambda: False)
mock_is_ubuntu = mock.patch('genes.ubuntu.traits.is_ubuntu', lambda: False)
mock_is_debian.start()
mock_is_ubuntu.start()

# Import apt now, triggering the mocks
reload_module(genes.apt.commands)

@mock.patch('genes.apt.commands.Config.ENV_CALL')
def test_install_package_on_non_apt_system(mocked_env_call):
    install("test")
    assert(genes.apt.commands.is_ubuntu() == False)
    assert(genes.debian.traits.is_debian() == False)
    genes.apt.commands.Config.ENV_CALL.assert_not_called()


# Reset mocks
# FIXME: move these to a teardown method
mock_is_debian.stop()
mock_is_ubuntu.stop()
reload_module(genes.debian.traits)
reload_module(genes.ubuntu.traits)

# def test_install_package_on_apt_system(mocker):
#     """Test calling apt.install with one package
#     :param mocker: This is the pytest-mock harness.
#     """
#     #mocker.patch.object(genes.debian.traits, 'is_debian', return_value=True)
#     mocker.patch('genes.ubuntu.traits.is_ubuntu', return_value=True)
#     from .commands import install
#     mocker.patch('genes.apt.commands.Config.ENV_CALL')
#     install("test")
#     genes.apt.commands.Config.ENV_CALL.assert_called_once_with(['apt-get', '-y', 'install', 'test'])
#
#
# def test_install_package_on_non_apt_system2(mocker):
#     mocker.patch('genes.debian.traits.is_debian', return_value=False)
#     mocker.patch('genes.ubuntu.traits.is_ubuntu', return_value=False)
#     from .commands import install
#     mocker.patch('genes.apt.commands.Config.ENV_CALL')
#     install("test")
#     genes.apt.commands.Config.ENV_CALL.assert_called_once_with(['apt-get', '-y', 'install', 'test'])


# def test_install_packages(monkeypatch):
#     """Test calling apt install with multiple packages
#     :param monkeypatch: This is the py.test monkeypatching for mock.
#     """
#     # FIXME: this test should fail
#     def mocked_subprocess_call(*args, **kwargs):
#         cmd = " ".join(args[0])
#         assert(cmd == 'sudo -E apt-get -y install test1 test2')
#         env = kwargs.get('env', None)
#         assert(env is not None)
#         assert(env.get('DEBIAN_FRONTEND', None) == 'noninteractive')
#         return 0
#         return 0
#
#     monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
#     install("test1", "test2")
#
#
# def test_install_nothing(monkeypatch):
#     """Test calling apt install with no packages (failure)
#     :param monkeypatch: This is the py.test monkeypatching for mock.
#     """
#     def mocked_subprocess_call(*args, **kwargs):
#         # This should never be called
#         assert not args and not kwargs
#         assert False
#
#     monkeypatch.setattr(subprocess, 'call', mocked_subprocess_call)
#     install()
