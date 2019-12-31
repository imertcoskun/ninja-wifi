
import os
import subprocess
import time
from scapy.all import send, IP, ICMP



# def denetle():
# 	wifi = Wireless('wlp3s0')
# 	wifi.getMode()

# if not os.geteuid() == 0:
# 	print ("Run as root....")
# 	exit(1)

# # iface = input("iface gir......")
# def monitor_mod():

# 	if (os.system('iwconfig wlx6470022a2436 mode') == 'Monitor'):
# 		print ("reis zaten monitorda...")
# 		sys.exit(1)
# 	else:	
# 		os.system('ifconfig ' + iface + ' down')
# 		try:
# 			subprocess.call('airmon-ng ' + iface + 'start', shell=True)
# 		except:
# 			print ("monitor moda alamadim garavel hocam...")
# 			sys.exit(1)
# 		os.system('ifconfig ' + iface + ' up')

def dusur_reis():
	os.system('ifconfig ' + iface + ' down')
	# try:
	os.system('iwconfig ' + iface + ' mode managed')
	
		# time.sleep(3)
	os.system('ifconfig '+ iface + 'up')
	# except:
		print ("manage moda alamadim garavel hocam....")
		sys.exit(1)
		os.system('ifconfig ' + iface + ' up')
		os.system('')
		# return iface


def listele():
	subprocess.call('airodump-ng wlan0mon', shell=True)

def scv_ac():
	import csv
	with open('cikti1-01.csv','r', encoding='utf-8') as csv_dosyasi:
		reader = cs.reader(csv_dosyasi)
		for row in reader:
			kanallar['kanal'] = row.values[3]
		
print ("hi world...")

#spf kaydi nedir.....#
#prt kaydi nedir.....#
