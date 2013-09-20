#!/usr/bin/env python3

from webclient import WebClient
from dds import DirectionSolver

def main():
    dds = DirectionSolver()
    wcl = WebClient(dds)
    try:
        wcl.run("ws://tetrisj.jvmhost.net:12270/codenjoy-contest/ws", 'au')
    except Exception as e:
        raise

if __name__ == '__main__':
    main()
