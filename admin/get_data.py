#!/usr/bin/python3
import time
import paramiko as ssh
import sys
import getpass

ssh_client=ssh.SSHClient()
ssh_client.set_missing_host_key_policy(ssh.AutoAddPolicy())
passwd = getpass.getpass(prompt = "Please type password:")



def get_all(list):
    for i in list:
        print(f"this is for {i}", end="")
        host = i.strip()
        port = "22"
        user = "shri"
        command = " uname -n ; uptime"
        ssh_client.connect(hostname=host, port=22, username=user, password=passwd)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdout = stdout.readlines()
        print(stdout)


nodes=open("/home/shri/python/sk_learn_practice/admin/kk")

get_all(nodes)



