#!/usr/bin/python2

import paramiko as ssh
import time
import os 
import sys
import getpass

ssh_client = ssh.SSHClient()
ssh_client.set_missing_host_key_policy(ssh.AutoAddPolicy)

passwd = getpass.getpass(prompt = "please type password : ")

def get_data(list):
    for j in list:
        print "This is for", j
        host = j.strip()
        port = 22
        user = "shri"
        command = "uptime ;uname -n"
        ssh_client.connect(hostname=host, port=port, username=user, password=passwd)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdout = stdout.readlines()
        print(stdout)
nodes=open("/home/shri/python/sk_learn_practice/admin/kk")




get_data(nodes)
