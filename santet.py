## santet-online 08-03-2018 (12:12)
# -*- coding: utf-8 -*-
# BlackHole Security
##
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils

netcatrat_banner = ""
facebookspam_banner = ""
smsbomber_banner = ""
smsspoofelk_banner = ""
telegramspam_banner = ""
denialofserviceattack_banner = ""

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print(backtomenu_banner)
	backtomenu = input("santet > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nERROR: Wrong input")
		time.sleep(2)
		restart_program()
		
__banner__ = ""
		
print(__banner__)
print("""
Select from the menu:
  01) Telegram Spam Message Attack
  00) Exit the Santet
""")
while True:
	try:
		santet = input("santet > ")
		
		if santet == "01" or santet == "1":
			print(telegramspam_banner)
			api_id = 1148490
			api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			client = TelegramClient("new",api_id,api_hash).start()
			target = input("santet > set USERNAME/ID ")
			try: count = int(input("santet > set COUNT "))
			except(ValueError): count = 999999
			urmsg = input("santet > set MESSAGE ")
			for x in range(count):
				client.send_message(target, urmsg)
				sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, target))
				sys.stdout.flush()
			print("\n[!] Done ... !!\n")
		elif santet == "00" or santet == "0":
			sys.exit()
		elif santet.lower() == "help":
			print(help_msg)
		elif santet.lower() == "banner":
			print(__banner__)
		elif santet.lower() == "clear":
			clearscreen()
		elif santet.lower() == "restart":
			restart_program()
		elif santet.lower() == "contact":
			print("Instagram: @dtlily\nTelegram: @dtlily\nFacebook: cgi.izo\nGitHub: Gameye98\nGitLab: dtlily\nYoutube: dtlily")
		elif santet.lower() == "about":
			print("Version 1.1\n\nCopyright (C) 2019 by DedSecTL\n\nDedSecTL\nCvar1984\nCiKu370\nMr.TenSwapper07\namsitlab\n[M]izuno\n3RROR_TMX\nMr.K3N\nZetSec\nTroublemaker97\nL_Viole\nX14N23N6\nMR.R45K1N\nlord.zephyrus\n4cliba788\nmr0x100\nMrx04\nViruz\nMr_007\nITermSec\nIdannovita.\nBlackHole Security.")
		elif santet.lower() == "version":
			print("Version 1.1")
		elif santet.lower() == "exit":
			sys.exit()
		else:
			pass
	except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
		print("The phone number is invalid (caused by SendCodeRequest)")
		print("You need to register your phone number first into Telegram\n")
	except(KeyboardInterrupt):
		print("\n[!] Close the program...")
		break
	except(EOFError):
		print("\n[!] Close the program...")
		break