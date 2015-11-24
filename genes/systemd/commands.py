#!/usr/bin/env python
from subprocess import Popen

def systemctl():
    pass


def start(service):
    Popen(['systemctl', 'start', service])


def stop(service):
    pass


def restart(service):
    Popen(['systemctl', 'restart', service])


def reload():
    pass
