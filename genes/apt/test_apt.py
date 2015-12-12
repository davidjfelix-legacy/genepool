#!/usr/bin/env python
from unittest import TestCase, mock

from .commands import install, recv_keys, update, upgrade, add_repo


class TestAptCommands(TestCase):
    @mock.patch('genes.apt.commands.env_run')
    def test_installing_package_should_call_popen(self, mock_run):
        """Test calling apt.install with one package"""
        install.__wrapped__('test')
        mock_run.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_installing_packages_should_call_popen(self, mock_run):
        """Test calling apt install with multiple packages"""
        install.__wrapped__('test1', 'test2')
        mock_run.assert_called_once_with(
            ['apt-get', '-y', 'install', 'test1', 'test2'])

    @mock.patch('genes.apt.commands.env_run')
    def test_install_nothing_should_error_and_not_call_popen(self, mock_run):
        self.assertRaises(ValueError, install.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_key_should_call_popen(self, mock_run):
        recv_keys.__wrapped__('test')
        mock_run.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80',
             '--recv-keys', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_keys_should_call_popen(self, mock_run):
        recv_keys.__wrapped__('test1', 'test2')
        mock_run.assert_called_once_with(
            ['apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80',
             '--recv-keys', 'test1', 'test2'])

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_keys_nothing_should_error_and_not_call_popen(
            self,
            mock_run):
        self.assertRaises(ValueError, recv_keys.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_update_should_call_popen(self, mock_run):
        update.__wrapped__()
        mock_run.assert_called_once_with(
            ['apt-get', '-y', 'update'])

    @mock.patch('genes.apt.commands.env_run')
    def test_upgrade_should_call_popen(self, mock_run):
        upgrade.__wrapped__()
        mock_run.assert_called_once_with(
            ['apt-get', '-y', 'upgrade'])

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_nothing_should_error_and_not_call_popen(self, mock_run):
        self.assertRaises(ValueError, add_repo.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_item_should_call_popen(self, mock_run):
        add_repo.__wrapped__("test")
        mock_run.assert_called_once_with(
            ['add-apt-repository', '-y', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_items_should_call_popen(self, mock_run):
        add_repo.__wrapped__("test1", "test2")
        mock_run.assert_called_once_with(
            ['add-apt-repository', '-y', 'test1 test2'])
