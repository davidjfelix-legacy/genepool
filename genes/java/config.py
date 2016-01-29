#!/usr/bin/env python
from collections import namedtuple


JavaConfig = namedtuple('JavaConfig', ['is_oracle', 'version'])


def config():
    return JavaConfig(
        is_oracle=True,
        version='oracle-java8',
    )

