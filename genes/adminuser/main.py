from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu
from genes.user.config import UserConfig
from genes import user


def main():
    # TODO: generalize for linux
    if is_debian() or is_ubuntu():
        def config_adminuser():
            return UserConfig(
                username='splicer',
                groups=['sudo'],
            )
        user.main(config_adminuser)
    elif is_osx():
        def config_adminuser():
            return UserConfig(
                username='splicer',
                groupes=['wheel'],
            )
        user.main(config_adminuser)
    else:
        # TODO: Handle others &windows fail otherwise
        pass
