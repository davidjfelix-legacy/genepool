from genes import apt, brew, pacman, http_downloader, checksum, msiexec
import platform


opsys = platform.system()
dist = platform.linux_distribution()


if platform == 'Linux' and dist == 'Arch':
    pacman.update()
    pacman.sync('go')


if platform == 'Linux' and (dist == 'Debian' or dist == 'Ubuntu'):
    apt.update()
    apt.install('golang')
    # TODO: make this a runner and require a switch to enable this
    apt.install('golang-go-darwin-amd64',
                'golang-go-freebsd-amd64',
                'golang-go-netbsd-amd64',
                'golang-go-windows-amd64')


if platform == 'Darwin':
    brew.update()
    brew.install('go')


if platform == 'Windows':
    installer = http_downloader.get('https://storage.googleapis.com/golang/go1.5.1.windows-amd64.msi')
    checksum.check(installer, 'sha1', '0a439f49b546b82f85adf84a79bbf40de2b3d5ba')
    install_flags = ('/qn' '/norestart')
    msiexec.run(installer, install_flags)
