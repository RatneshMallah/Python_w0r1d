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

def add_repo():
	try:
		os.system("sudo add-apt-repository ppa:noobslab/macbuntu -y")
		os.system("sudo apt-get update")
		print(10*"*","\nRepo added!\n",10*"*")
	except:
		print("Can't add repo")
		sys.exit()


def install_theme():
	try:
		os.system("sudo apt-get install macbuntu-os-icons-v1804 -y")
		os.system("sudo apt-get install macbuntu-os-ithemes-v1804 -y")
		print(10*"*","\nTheme installed!\n",10*"*")
	except:
		print("Can't install theme")
		sys.exit()


def install_plank():
	try:
		os.system("sudo apt-get install plank -y")
		print(10*"*","\nPlank installed!\n",10*"*")
	except:
		print("Can't install Plank")
		sys.exit()

def install_plank_theme():
	try:
		os.system("sudo add-apt-repository ppa:noobslab/macbuntu -y")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install macbuntu-os-plank-theme-v1804 -y")
		print(10*"*","\nPlank theme installed!\n",10*"*")
	except:
		print("Can't install Plank theme")
		sys.exit()


#check_root()
add_repo()
install_theme()
install_plank()
install_plank_theme()