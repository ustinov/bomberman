#!/usr/bin/env python3

from sys import argv
from sys import version_info
from webclient import WebClient
from dds import DirectionSolver

_SERVER = "ws://172.22.108.60:8080/codenjoy-contest/ws"

def main(username):

    assert version_info[0] == 3, "You should run me with Python 3.x"

    dds = DirectionSolver()
    wcl = WebClient(dds)

    wcl.run(_SERVER, username)

if __name__ == '__main__':
    assert argv[1], "You should have to pass the username as a parameter."
    main(argv[1])
