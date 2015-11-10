import platform
from .traits import is_debian


def test_is_debian(monkeypatch):
    """Test the is_debian helper function when it is Debian"""
    def mocked_platform_system(*args, **kwargs):
        return 'Linux'

    def mocked_platform_dist(*args, **kwargs):
        return 'Debian', -1, 'spam'

    monkeypatch.setattr(platform, 'system', mocked_platform_system)
    monkeypatch.setattr(platform, 'linux_distribution', mocked_platform_dist)
    assert is_debian()


def test_is_not_debian(monkeypatch):
    """Test the is_debian helper function when it is not Debian"""
    def mocked_platform_system(*args, **kwargs):
        return 'Spam'

    def mocked_platform_dist(*args, **kwargs):
        return 'Spam', -1, 'eggs'

    monkeypatch.setattr(platform, 'system', mocked_platform_system)
    monkeypatch.setattr(platform, 'linux_distribution', mocked_platform_dist)
    assert(is_debian() == False)
