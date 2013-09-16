#!/usr/bin/env python3

from webclient import WebClient

def main():
    dds = None
    wcl = WebClient(dds)
    try:
        wcl.run("ws://tetrisj.jvmhost.net:12270/codenjoy-contest/ws",
                'lishmael')
    except Exception as e:
        raise

if __name__ == '__main__':
    main()
