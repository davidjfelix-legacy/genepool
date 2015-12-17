from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu
from genes.user import UserBuilder


def main():
    # TODO: generalize for linux
    if is_debian() or is_ubuntu():
        UserBuilder('splicer').\
            add_group('sudo').\
            build()
    elif is_osx():
        UserBuilder('splicer').\
            add_group('admin').\
            build()
    else:
        # TODO: Handle others &windows fail otherwise
        pass
