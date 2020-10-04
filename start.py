import sys
import subprocess 
import os
import pyttsx3
from decouple import config

IP_ROUTER = config('IP_ROUTER')
IP_DEVICE = config('IP_DEVICE')

saytxt = "Someone has connected to the network"
engine = pyttsx3.init()

proc = subprocess.Popen(["ping", '-t', IP_DEVICE],stdout=subprocess.PIPE)

while True:
	line = proc.stdout.readline()
	if not line:
		break
	else:
		None

	try:
		connected_ip = line.decode('utf-8').split()[2].replace(':', '')
		if connected_ip == IP_DEVICE:
			engine.say(saytxt)
			engine.runAndWait()
			break
		else:
			print('Pinging device...')
	except:
		pass
