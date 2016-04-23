from unittest import TestCase
from unittest.mock import patch

from genes.apt.key import APTKey


class APTKeyInitTestCase(TestCase):
    def test_init_should_get_deps_if_both_missing(self):
        with patch('genes.apt.key.APTPkg.is_installed') as mock_apt_pkg, \
                patch('genes.apt.key.APTGet.update') as mock_update, \
                patch('genes.apt.key.APTGet.install') as mock_install:
            mock_apt_pkg.return_value = False
            APTKey()
            mock_update.assert_called_with()
            mock_install.assert_called_once_with('apt-transport-https', 'ca-certificates')

    def test_init_should_get_deps_if_either_missing(self):
        with patch('genes.apt.key.APTPkg.is_installed') as mock_apt_pkg, \
                patch('genes.apt.key.APTGet.update') as mock_update, \
                patch('genes.apt.key.APTGet.install') as mock_install:
            def partially_installed(value):
                return value == 'ca-certificates'

            mock_apt_pkg.side_effect = partially_installed
            APTKey()
            mock_update.assert_called_with()
            mock_install.assert_called_once_with('apt-transport-https', 'ca-certificates')

    def test_init_should_not_get_deps_if_both_installed(self):
        with patch('genes.apt.key.APTPkg.is_installed') as mock_apt_pkg, \
                patch('genes.apt.key.APTGet.update') as mock_update, \
                patch('genes.apt.key.APTGet.install') as mock_install:
            mock_apt_pkg.return_value = True
            APTKey()
            mock_update.assert_not_called()
            mock_install.assert_not_called()


class APTKeyRecvKeyTestCase(TestCase):
    def test_recv_keys_should_call_popen(self):
        with patch('genes.process.process.Popen') as mock_popen:
            APTKey.recv_keys('test')
            mock_popen.assert_called_once_with(
                    ('apt-key', 'adv', '--keyserver', 'hkp://pgp.mit.edu:80', '--recv-keys', 'test')
            )
