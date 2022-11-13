#l/bin/python
import os,sys,time
love = '''
\033[1;31mm##m##m       m##m##m       m##m##m       m##m##m
"######       "######       "######       "######
 "###"         "###"         "###"         "###"
   "             "             "             " '''
wrng = '''
__          __     _____  _   _ _____ _   _  _____
\ \        / /\   |  __ \| \ | |_   _| \ | |/ ____|
 \ \  /\  / /  \  | |__) |  \| | | | |  \| | |  __
  \ \/  \/ / /\ \ |  _  /| . ` | | | | . ` | | |_ |
   \  /\  / ____ \| | \ \| |\  |_| |_| |\  | |__| |
    \/  \/_/    \_\_|  \_\_| \_|_____|_| \_|\_____|'''

identitas = '''
   ×---------------------------------------------------×
    [*]github:https://github.com/bocilkematian1
    [*]youtube:AZZA_4224
    [*]email:azzaganz123@gmail.com
    [*]tik tok:AZZA:042240  (gone adex)
    [*]omlet arcade:AZZA_4224
    [*]wa:081333000236
   ×---------------------------------------------------×
'''

def clear () :
	os.system('clear')
import os,sys,time

def sleep () :
	time.sleep (0.1)
def error () :
	err()
	err()
	err()
	err()
	err()
def iden () :
	puas = input ("wes puas?(y)")
	if puas == 'y' :
		ganti()
	else :
		print ("pileh tenanan lah...")
		time.sleep (1)
		iden()
def err () :
	print ("\033[1;32mDownloading https://files.pythonhosted.org/packa>")
	sleep()
	print ("Looking in links: /data/data/com.termux/files/usr/tmp/>")
	sleep()
	print ("[*] https://packages-cf.termux.org/apt/termux-main/: ok")
	sleep()
	print ("Building dependency tree... Done")
def ganti ():
	clear()
	print (wrng)
	pndpt = input ("\033[1;33mmeh ganti pendapat ra??\033[1;32m(y/n)")
	if pndpt == 'y' :
		ya()
	if pndpt == 'n' :
		print ("\033[1;31mIKI OJO NGASI IKI BOCOR NAK BOCOR....")
		time.sleep (3)
		error()
		error()
		error()
		error()
		error()
		exit()
	else :
		print ("pileh tenanan lah....")
		time.sleep (1)
		ganti()
def ya ():
	clear()
	print (love)
	print ("")
	print ("")
	time.sleep (1)
	glm = input ("\033[1;31m》 gelem ra dadi pacarku?\033[1;32m(y/n)")
	if glm == 'y' :
		os.system ('xdg-open https://wa.me/6285877522132?text=ya')
		print (identitas)
		iden()
		ganti()
	if glm == 'n' :
		os.system ('xdg-open https://wa.me/6285877522132?text=tidak')
		ganti()
	else :
		print ("pileh tenanan lah.....")
		time.sleep (1)
		ya()

def menu ():
	time.sleep (0.3)
	clear()
	os.system ("figlet HELLO|lolcat -a")
	print ("")
	time.sleep (1)
	print ("\033[1;37m  •>>\033[1;35maku jane wes suwe seneng ro kowe")
	print ("\033[0;31m==============================================》")
	time.sleep(1)
	print ("\033[1;37m  •>>\033[1;35mtapi aku ra tau ngetokke")
	print ("\033[0;31m============================》")
	time.sleep (1)
	print ("\033[1;37m  •>>\033[1;35maku sak kelas karo kowe smp/madrasah")
	print ("\033[0;31m==================================================》")
	time.sleep (1)
	print ("")
	print ("")
	print ("")
	nama = input ("\033[1;33mpengen ngerti ra aku sopo?\033[1;32m(y/n)")
	if nama == 'y' :
		ya()
	if nama == 'n' :
		print ("yowes")
		exit()
	else :
		print ("pileh tenanan lah......")
		time.sleep (1)
		menu()

menu()
