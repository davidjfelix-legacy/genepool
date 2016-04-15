from unittest import TestCase


class TestDockerPkg(TestCase):
    def test_install_on_ubuntu_should_run_apt(self):
        # FIXME: need to find a good way to set OS functions all at once
        pass

    def test_install_on_debian_should_run_apt(self):
        pass

    def test_install_on_osx_should_run_brew(self):
        pass
