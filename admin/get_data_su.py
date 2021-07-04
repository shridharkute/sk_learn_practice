#!/usr/bin/python3
# This script can be used to execute sudo comamnd


import getpass
import time
import sys
import paramiko as ssh
import os

ssh_client = ssh.SSHClient()
ssh_client.set_missing_host_key_policy(ssh.AutoAddPolicy())


nodes=open("/home/shri/python/sk_learn_practice/admin/kk")

user="shri"
sudoPassword=getpass.getpass(prompt="Plese type sudo password: ")


def execute_command(list):
    for i in list:
        print(f"This is for {i}")
        command = "ls -lrth /root"
        host = i.strip()
        ssh_client.connect(hostname=host,port=22,username=user,password=sudoPassword)
        #stdin, stdout, stderr = ssh_client.exec_command(command)
        os.system('echo %s | sudo -S %s' % (sudoPassword, command))
        #stdout = stdout.readlines()
        #print(stdout)

execute_command(nodes)
        
