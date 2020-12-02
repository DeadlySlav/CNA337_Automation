# This is the template code for the CNA337 Final Project
# Eric Yevenko
# CNA 337 Fall 2020
#Worked with Dylan McCormack, Michael Horton
#Received help from Luma
import os
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        server = os.system("ping -n 4 " + self.server_ip)
        return self.server_ip
