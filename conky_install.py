__author__ = "$R.K.M.$"

import os
import time
import sys

def check_root():
	try:
		os.system("sudo su")
		print(10*"*","\nRoot accessed!\n",10*"*")
	except:
		print("You have not give root access!")
		sys.exit()

def install_conky():
	try:
		os.system("sudo apt-get install conky conky-all -y")
		os.system("cd && wget -O .start-conky http://drive.noobslab.com/data/conky/start-conky")
		os.system("chmod +x .start-conky")
		print(10*"*","\nConky installed!\n",10*"*")
	except:
		print("Can't install conky")
		sys.exit()

def install_conky_for_4_cpu():
	try:
		os.system("cd && wget -O colors-noobslab-2.zip http://drive.noobslab.com/data/conky/colors/colors-conky-2cpu.zip")
		os.system("unzip colors-noobslab-2.zip && rm colors-noobslab-2.zip")
		print(10*"*","\ninstalled conky for 4 cpu!\n",10*"*")
	except:
		print("Can't install conky for 4 cpu")
		sys.exit()


install_conky()
install_conky_for_4_cpu()