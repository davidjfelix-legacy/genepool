from unittest import TestCase
from unittest.mock import patch

from genes.apt.get import APTGet


class TestAPTGetInstall(TestCase):
    def test_apt_get_install_no_items_fails(self):
        with patch('genes.process.process.Popen') as mock_popen:
            apt_get = APTGet()
            with self.assertRaises(ValueError):
                apt_get.install()
            mock_popen.assert_not_called()

    def test_apt_get_install_single_item_calls_popen(self):
        with patch('genes.process.process.Popen') as mock_popen:
            apt_get = APTGet()
            apt_get.install('test')
            mock_popen.assert_called_with(('apt-get', '-y', 'install', 'test'))

    def test_apt_get_install_multiple_items_calls_popen(self):
        with patch('genes.process.process.Popen') as mock_popen:
            apt_get = APTGet()
            apt_get.install('test1', 'test2')
            mock_popen.assert_called_once_with(('apt-get', '-y', 'install', 'test1', 'test2'))


class TestAPTGetUpdate(TestCase):
    def test_apt_get_update_calls_popen(self):
        with patch('genes.process.process.Popen') as mock_popen:
            apt_get = APTGet()
            apt_get.update()
            mock_popen.assert_called_once_with(('apt-get', '-y', 'update'))


class TestAPTGetUpgrade(TestCase):
    def test_apt_get_upgrade_with_no_items_calls_popen(self):
        with patch('genes.process.process.Popen') as mock_popen:
            apt_get = APTGet()
            apt_get.upgrade()
            mock_popen.assert_called_once_with(('apt-get', '-y', 'upgrade'))

