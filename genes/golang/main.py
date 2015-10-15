from genes import apt, brew
import platform


opsys = platform.system()
dist = platform.linux_distribution()

def main():
    if platform == 'Linux' and (dist == 'Debian' or dist == 'Ubuntu'):
        apt.update()
        apt.install('golang')
        # TODO: make this a runner and require a switch to enable this
        apt.install('golang-go-darwin-amd64',
                    'golang-go-freebsd-amd64',
                    'golang-go-netbsd-amd64',
                    'golang-go-windows-amd64')
