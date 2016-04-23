from genes.package import Package


class AdminUser(Package):
    def uninstall(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        pass

    def is_installed(self, *args, **kwargs):
        pass

    def install(self, *args, **kwargs):
        # TODO: user/group to create:
        # debian/ubuntu -> splicer/sudo
        # osx -> splicer/wheel
        pass
