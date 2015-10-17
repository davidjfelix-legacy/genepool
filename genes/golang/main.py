from genes import apt, brew
from genes.ubuntu import is_ubuntu
from genes.debian import is_debian
from genes.mac import is_osx



def main():
    if is_ubuntu() or is_debian():
        apt.update()
        apt.install('golang')
        # TODO: make this a runner and require a switch to enable this
        apt.install('golang-go-darwin-amd64',
                    'golang-go-freebsd-amd64',
                    'golang-go-netbsd-amd64',
                    'golang-go-windows-amd64')

    if is_osx():
        brew.update()
        brew.install('go')
