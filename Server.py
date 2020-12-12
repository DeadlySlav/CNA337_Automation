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

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('3.23.115.46', port=22, username='ec2-user', password='', key_filename=r'C:\Users\Eric\.ssh\id_rsa')

stdin, stdout, stderr = ssh.exec_command('sudo yum update; sudo yum upgrade')
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()
