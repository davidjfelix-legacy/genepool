#!/usr/bin/env python
from unittest import TestCase, mock

from .commands import install, recv_keys, Config


class TestAptCommands(TestCase):
    @mock.patch('genes.apt.commands.Popen')
    def test_install_package_on_non_apt_system(self, mock_popen):
        install.__wrapped__('test')
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_install_package_on_debian_system(self, mock_popen):
        """Test calling apt.install with one package"""
        install.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_install_package_on_ubuntu_system(self, mock_popen):
        """Test calling apt.install with one package"""
        install.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_install_packages(self, mock_popen):
        """Test calling apt install with multiple packages"""
        install.__wrapped__('test1', 'test2')
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test1', 'test2'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_install_nothing(self, mock_popen):
        install.__wrapped()
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_key_on_non_apt_system(self, mock_popen):
        recv_keys.__wrapped__()
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_key_on_a_debian_system(self, mock_popen):
        recv_keys.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hpk://pgp.mit.edu:80', '--recv-keys', 'test'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_key_on_an_ubuntu_system(self, mock_popen):
        recv_keys.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hpk://pgp.mit.edu:80', '--recv-keys', 'test'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_keys_on_an_apt_system(self, mock_popen):
        recv_keys.__wrapped__('test1', 'test2')
        mock_popen.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hpk://pgp.mit.edu:80', '--recv-keys', 'test1', 'test2'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_keys_nothing(self, mock_popen):
        recv_keys.__wrapped__()
        mock_popen.assert_not_called()
