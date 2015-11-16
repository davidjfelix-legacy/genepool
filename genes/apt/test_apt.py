#!/usr/bin/env python
from unittest import mock, TestCase
import genes
from .commands import install, Config


class TestAptCommands(TestCase):

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=False)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=False)
    def test_install_package_on_non_apt_system(
            self, mock_is_ubuntu, mock_is_debian, mock_env_call):
        install("test")
        self.assertFalse(genes.apt.commands.is_ubuntu())
        self.assertFalse(genes.apt.commands.is_debian())
        assert not mock_env_call.called

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=True)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=False)
    def test_install_package_on_debian_system(
            self, mock_is_ubuntu, mock_is_debian, mock_env_call):
        """Test calling apt.install with one package"""
        install("test")
        self.assertTrue(genes.apt.commands.is_debian())
        self.assertFalse(genes.apt.commands.is_ubuntu())
        mock_env_call.assert_called_once_with(['apt-get', '-y', 'install', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=False)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=True)
    def test_install_package_on_ubuntu_system(self, mock_is_ubuntu, mock_is_debian, mock_env_call):
        """Test calling apt.install with one package"""
        install("test")
        self.assertFalse(genes.apt.commands.is_debian())
        self.assertTrue(genes.apt.commands.is_ubuntu())
        mock_env_call.assert_called_once_with(['apt-get', '-y', 'install', 'test'], env=Config.ENV)



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
