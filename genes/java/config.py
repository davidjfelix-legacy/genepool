#!/usr/bin/env python


class JavaConfigurator(object):
    _oracle_versions = (
        "oracle-java6",
        "oracle-java7",
        "oracle-java8",
    )
    _versions = (
        "openjdk6",
        "openjdk7",
        "openjdk8",
        "oracle-java6",
        "oracle-java7",
        "oracle-java8",
    )

    def __init__(self):
        self._version = "oracle-java8"

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        # TODO: add a bunch of os specific stuff here
        if version in self._versions:
            self._version = version
        else:
            # FIXME: add logging, error handling, etc
            pass

    def set_version(self, version, override=False):
        if override:
            self._version = version
        else:
            self.version = version

    def is_oracle(self):
        return self._version in self._oracle_versions
