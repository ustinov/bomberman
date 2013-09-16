#!/usr/bin/env python3

from websocket import WebSocketApp

class WebClient(WebSocketApp):

    def __init__(self, solver = None):
        #assert solver not None
        self._solver = solver
        self._server = None
        self._user = None

    def run(self, server, user):
        super().__init__("{}?user={}".format(server, user))
        self.on_message = _on_message
        self.on_open = _on_open
        self._server = server
        self._user = user
        self.run_forever()
    
def _on_open(webclient):
    print("Opening Connection...")
    print("Sending Command <UP>...")
    webclient.send("UP")

def _on_message(webclient, message):
    m = message.lstrip("board=")
    [print(m[i:i + 33]) for i in range(0, len(m), 33)]


def _on_error(webclient, error):
    print(error)
