from unittest import TestCase
from unittest.mock import patch, call

from genes.docker.package import DockerPkg


class TestDockerPkg(TestCase):
    def test_install_on_ubuntu_should_run_apt(self):
        with patch('genes.docker.package.get_os') as mock_get_os:
            mock_get_os.return_value = 'ubuntu'
            with patch('genes.process.process.Popen') as mock_popen:
                with patch('genes.docker.package.DockerPkg.add_deb_repository') as mock_add_repo:
                    docker_pkg = DockerPkg()
                    docker_pkg.install()
                    calls = [
                        call(('apt-get', '-y', 'update')),
                        call().wait(),
                        call(('apt-get', '-y', 'install', 'docker-engine')),
                        call().wait(),
                    ]
                    mock_add_repo.assert_called_once_with()
                    mock_popen.assert_has_calls(calls)

    def test_install_on_debian_should_run_apt(self):
        with patch('genes.docker.package.get_os') as mock_get_os:
            mock_get_os.return_value = 'debian'
            with patch('genes.process.process.Popen') as mock_popen:
                with patch('genes.docker.package.DockerPkg.add_deb_repository') as mock_add_repo:
                    docker_pkg = DockerPkg()
                    docker_pkg.install()
                    calls = [
                        call(('apt-get', '-y', 'update')),
                        call().wait(),
                        call(('apt-get', '-y', 'install', 'docker-engine')),
                        call().wait(),
                    ]
                    mock_add_repo.assert_called_once_with()
                    mock_popen.assert_has_calls(calls)

    def test_install_on_osx_should_run_brew(self):
        with patch('genes.docker.package.get_os') as mock_get_os:
            mock_get_os.return_value = 'osx'
            with patch('genes.process.process.Popen') as mock_popen:
                with patch('genes.docker.brew.cask.is_installed') as mock_cask_is_installed:
                    mock_cask_is_installed.return_value = True
                    docker_pkg = DockerPkg()
                    docker_pkg.install()
                    calls = [
                        call(('brew', 'cask', 'update')),
                        call().wait(),
                        call(('brew', 'cask', 'install', 'dockertoolbox')),
                        call().wait(),
                    ]
                    mock_popen.assert_has_calls(calls)
