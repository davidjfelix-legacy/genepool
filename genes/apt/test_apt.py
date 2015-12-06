#!/usr/bin/env python
from unittest import TestCase, mock

from .commands import install, recv_keys, update, Config, upgrade, add_repo


class TestAptCommands(TestCase):
    @mock.patch('genes.apt.commands.Popen')
    def test_installing_package_should_call_popen(self, mock_popen):
        """Test calling apt.install with one package"""
        install.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_installing_packages_should_call_popen(self, mock_popen):
        """Test calling apt install with multiple packages"""
        install.__wrapped__('test1', 'test2')
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test1', 'test2'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_install_nothing_should_error_and_not_call_popen(self, mock_popen):
        self.assertRaises(ValueError, install.__wrapped__)
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_key_should_call_popen(self, mock_popen):
        recv_keys.__wrapped__('test')
        mock_popen.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hpk://pgp.mit.edu:80',
             '--recv-keys', 'test'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_keys_should_call_popen(self, mock_popen):
        recv_keys.__wrapped__('test1', 'test2')
        mock_popen.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hpk://pgp.mit.edu:80',
             '--recv-keys', 'test1', 'test2'],
            env=Config.ENV
        )

    @mock.patch('genes.apt.commands.Popen')
    def test_recv_keys_nothing_should_error_and_not_call_popen(
            self,
            mock_popen):
        self.assertRaises(ValueError, recv_keys.__wrapped__)
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_update_should_call_popen(self, mock_popen):
        update.__wrapped__()
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'update'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_upgrade_should_call_popen(self, mock_popen):
        upgrade.__wrapped__()
        mock_popen.assert_called_once_with(
            ['apt-get', '-y', 'upgrade'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_add_repo_nothing_should_error_and_not_call_popen(
            self,
            mock_popen):
        self.assertRaises(ValueError, add_repo.__wrapped__)
        mock_popen.assert_not_called()

    @mock.patch('genes.apt.commands.Popen')
    def test_add_repo_item_should_call_popen(self, mock_popen):
        add_repo.__wrapped__("test")
        mock_popen.assert_called_once_with(
            ['add-apt-repository', '-y', 'test'], env=Config.ENV)

    @mock.patch('genes.apt.commands.Popen')
    def test_add_repo_items_should_call_popen(self, mock_popen):
        add_repo.__wrapped__("test1", "test2")
        mock_popen.assert_called_once_with(
            ['add-apt-repository', '-y', 'test1 test2'], env=Config.ENV)
