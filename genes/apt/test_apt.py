#!/usr/bin/env python
try:
    import mock
except ImportError:
    from unittest import mock

from unittest import TestCase
import genes
from .commands import install, Config


class TestAptCommands(TestCase):

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=False)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=False)
    def test_install_package_on_non_apt_system(
            self, mock_is_ubuntu, mock_is_debian, mock_popen):
        install("test")
        self.assertFalse(genes.apt.commands.is_ubuntu())
        self.assertFalse(genes.apt.commands.is_debian())
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=True)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=False)
    def test_install_package_on_debian_system(
            self, mock_is_ubuntu, mock_is_debian, mock_env_call):
        """Test calling apt.install with one package"""
        install("test")
        self.assertTrue(genes.apt.commands.is_debian())
        self.assertFalse(genes.apt.commands.is_ubuntu())
        mock_env_call.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=False)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=True)
    def test_install_package_on_ubuntu_system(
            self, mock_is_ubuntu, mock_is_debian, mock_popen):
        """Test calling apt.install with one package"""
        install("test")
        self.assertFalse(genes.apt.commands.is_debian())
        self.assertTrue(genes.apt.commands.is_ubuntu())
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=True)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=True)
    def test_install_packages(
            self, mock_is_ubuntu, mock_is_debian, mock_popen):
        """Test calling apt install with multiple packages"""
        install("test1", "test2")
        self.assertTrue(genes.apt.commands.is_debian())
        self.assertTrue(genes.apt.commands.is_ubuntu())
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test1', 'test2'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    @mock.patch('genes.apt.commands.is_debian', return_value=True)
    @mock.patch('genes.apt.commands.is_ubuntu', return_value=True)
    def test_install_nothing(
            self, mock_is_ubuntu, mock_is_debian, mock_popen):
        install()
        self.assertTrue(genes.apt.commands.is_debian())
        self.assertTrue(genes.apt.commands.is_ubuntu())
        mock_popen.assert_not_called()
