#!/usr/bin/env python
from unittest import TestCase, mock

from .commands import install, recv_keys, update, upgrade, add_repo, add_ppa


class TestAptCommands(TestCase):
    """A unittest testing class for the apt commands"""

    @mock.patch('genes.apt.commands.env_run')
    def test_installing_package_should_call_popen(self, mock_run):
        """Test calling apt.install with one package"""
        install.__wrapped__('test')
        mock_run.assert_called_once_with(
                ['apt-get', '-y', 'install', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_installing_packages_should_call_popen(self, mock_run):
        """Test calling apt.install with multiple packages"""
        install.__wrapped__('test1', 'test2')
        mock_run.assert_called_once_with(
                ['apt-get', '-y', 'install', 'test1', 'test2'])

    @mock.patch('genes.apt.commands.env_run')
    def test_install_nothing_should_error_and_not_call_popen(self, mock_run):
        """Test calling apt.install with nothing"""
        self.assertRaises(ValueError, install.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_key_should_call_popen(self, mock_run):
        """Test calling apt.recv_keys with one key"""
        recv_keys.__wrapped__('test')
        mock_run.assert_called_once_with(
                ['apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80',
                 '--recv-keys', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_keys_should_call_popen(self, mock_run):
        """Test calling apt.recv_keys with multiple keys"""
        recv_keys.__wrapped__('test1', 'test2')
        mock_run.assert_called_once_with(
                ['apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80',
                 '--recv-keys', 'test1', 'test2'])

    @mock.patch('genes.apt.commands.env_run')
    def test_recv_keys_nothing_should_error_and_not_call_popen(self, mock_run):
        """Test calling apt.recv_keys with nothing"""
        self.assertRaises(ValueError, recv_keys.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_update_should_call_popen(self, mock_run):
        """Test calling apt.update"""
        update.__wrapped__()
        mock_run.assert_called_once_with(
                ['apt-get', '-y', 'update'])

    @mock.patch('genes.apt.commands.env_run')
    def test_upgrade_should_call_popen(self, mock_run):
        """Test calling apt.upgrade"""
        upgrade.__wrapped__()
        mock_run.assert_called_once_with(
                ['apt-get', '-y', 'upgrade'])

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_nothing_should_error_and_not_call_popen(self, mock_run):
        """Test calling apt.add_repo with nothing"""
        self.assertRaises(ValueError, add_repo.__wrapped__)
        mock_run.assert_not_called()

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_item_should_call_popen(self, mock_run):
        """Test calling apt.add_repo with one item"""
        add_repo.__wrapped__("test")
        mock_run.assert_called_once_with(
                ['add-apt-repository', '-y', 'test'])

    @mock.patch('genes.apt.commands.env_run')
    def test_add_repo_items_should_call_popen(self, mock_run):
        """Test calling apt.add_repo with multiple items"""
        add_repo.__wrapped__("test1", "test2")
        mock_run.assert_called_once_with(
                ['add-apt-repository', '-y', 'test1 test2'])

    @mock.patch('genes.apt.commands.env_run')
    def test_add_ppa_item_should_call_popen(self, mock_run):
        """Test calling apt.add_ppa with item"""
        add_ppa.__wrapped__("test")
        mock_run.assert_called_once_with(
                ['add-apt-repository', '-y', 'ppa:test'])
