from evolution_master.runners import pkg, download

# Install for Arch
with pkg.pacman() as pkg_man:
    pkg_man.install('go')

# Install for Debian & Ubuntu
with pkg.apt() as pkg_man:
    pkg_man.install('golang')
    # TODO: make this a runner and require a switch to enable this
    pkg_man.install('golang-go-darwin-amd64',
                    'golang-go-freebsd-amd64',
                    'golang-go-netbsd-amd64',
                    'golang-go-windows-amd64')

# Install for OSX
with pkg.brew() as pkg_man:
    pkg_man.install('go')

# Install for Windows
with  download.https() as downloader, pkg.msiexec() as installer:
    downloader.get('https://storage.googleapis.com/golang/go1.5.1.windows-amd64.msi')
    downloader.checksum('sha1', '0a439f49b546b82f85adf84a79bbf40de2b3d5ba')
    installer.install_flags('/qn' '/norestart')
    installer.await(downloader.finished())
