########################################
#
#           PANDORA API
#
#
#      Random data for testing
#
#
#
#           Matheus - 2021
#
########################################

import json, http.server, socketserver, socket
from random import randint
from random import choice
from typing import Tuple
from http import HTTPStatus


# Main configuration
class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: Tuple[str, int], 
                                server: socketserver.BaseServer):
        super().__init__(request, client_address, server)

    @property
    def api_response(self):
        ###########
        # Insert here everything that you want to access in your API!
        ##########
        
        # Pseudo random number generator config (min, max)
        jose = randint(0, 1000)   

        # More gimmicky
        pi = "3,14159265358979323846"   

        # Pseudo random name list
        # NOT USED ANYMORE
        paula = [" ", " ",
                " ", " "] 
        zeca_pagodinho = choice(paula)

        # Open a file/db and iterate through it
        with open("db.txt", "r") as db:
            # it splits at every new line
            lines = db.read().split('\n')
        # Pick randomly a whole line and spits it into
        # our json API
        for line in lines:
            joao = choice(lines)
                   
        #################
        # IMPORTANT !!!!
        # return the json here!
        # need to instanciate all the things that you want to
        # access through the API
        return json.dumps(
                {
                    "Random Message": joao,
                    "Random Number": jose,
                    "PI": pi
                }
                ).encode()

    # GET Prototype
    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(self.api_response))

    # POST Prototype
    """
    def do_POST(self):
        contentLength = int(self.headers['Content Length'])
        body = self.rfile.read(contentLength)
        self.sendResponse(200)
        self.endHeaders()
        response = BytesIO()
        response.write(b'POST REQUEST SENDED')
        response.write(b'RECEIVED POST REQUEST ')
        response.write(body)
        self.wfile.write(response.getvalue())
    """



# RUN
if __name__ == "__main__":
    PORT = 8000
    #MYIP = "192.168.0.26"
    # Gets dinamically the server IP to access it
    MYIP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MYIP.connect(("8.8.8.8", PORT))
    MYIP = MYIP.getsockname()[0]

    # Create the API server
    PANDORA_API = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
    print(f"Pandora API started @ {MYIP}:{PORT}")
    PANDORA_API.serve_forever()
