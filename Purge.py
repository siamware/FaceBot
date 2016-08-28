#!/usr/bin/env python2.7
#
# Blocks Friends & Deletes Photos For You, Good For Cleaning Up Old Facebook Accounts
#
# Designed For Kali Linux 2.0
#
from re import search
from time import sleep
from sys import exit,argv
from subprocess import call,Popen
from os import path,getuid,devnull
from threading import Thread, Lock
#
Devnull = open(devnull, 'w')
if getuid() != 0: call('clear');exit('[!] Please run this program with root access\n\nEx: sudo python {}'.format(argv[0]))
try: from selenium import webdriver;from selenium.webdriver.common.keys import Keys
except: call(['clear']);print'[+] Installing Selenium...';Popen(['sudo','pip','install','-U','selenium'],stdout=Devnull,stderr=Devnull).wait()
try: from selenium import webdriver;from selenium.webdriver.common.keys import Keys
except ImportError: call(['clear']);exit('[!] Need Selenium & PhantomJS To Run...') 
#

def Collect_Friends():
 global Run,On,Ran,Spin
 driver.get("https://www.facebook.com/{}/friends?source_ref=pb_friends_tl".format(str(name)))
 Ran = False
 while On:
  if len(Friends) == 0:
   with lock:
    if Spin >= 20: driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");Spin=0
    Elems = driver.find_elements_by_xpath("//a[@href][@tabindex='-1'][@aria-hidden='true']")
    for elem in Elems: 
     if Ran == False: Ran = True
     Link = str(elem.get_attribute("href"))
     if search('friends_tab',Link): 
      x=0
      Starts = 25
      for l in Link: 
       if l.strip() == str('?').strip() : End = int(x);break
       x+=1
      friend = str(Link[Starts:End]).strip()
      if not search(friend,str(Blocked)) and friend != 'profile.php'.strip(): 
       Friends.append(friend);Blocked.append(friend);
    if len(Friends) == 0 and Ran: driver.quit();Run = False;On=False

def Collect_Photos():
 global Run2,On2,Ran2,Spin2
 driver.get("https://www.facebook.com/{}/photos?source_ref=pb_friends_tl".format(str(name)))
 Ran2 = False
 while On2:
  if len(Photos) == 0:
   with lock:
    if Spin2 >= 20: driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");Spin2=0
    Elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in Elems: 
     if Ran2 == False: Ran2 = True
     Link = str(elem.get_attribute("href"))
     if search('photo.php',Link): 
      x=0
      Starts = 40
      for l in Link: x+=1
      End = int(x)
      photo = str(Link[Starts:End]).strip();
      if not search(photo,str(Deleted)): Photos.append(photo);Deleted.append(photo)
    if len(Photos) == 0 and Ran2: driver.quit();Run2 = False;On2=False
			  
def Login():
 call(['clear']);print '[-] Login In Progress...'
 username = driver.find_element_by_id("email")
 password = driver.find_element_by_id("pass")
 username.send_keys(name)
 password.send_keys(Pass) 
 call(['clear'])
 password.submit()
 CurrentUrl = str(driver.current_url).strip()
 if CurrentUrl != 'https://www.facebook.com/'.strip(): driver.quit();exit('[+] Incorrect Logins')
	
def Block_Friends():
 global Friends,Spin
 call(['clear']);print '[+] Reading Friends\' list...';sleep(1.7)
 with lock:
  Spin = 0
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  driver2 = webdriver.PhantomJS()
  driver2.implicitly_wait(1.3)
  driver2.maximize_window() 
  driver2.get("https://www.facebook.com");
  username = driver2.find_element_by_id("email")
  password = driver2.find_element_by_id("pass")
  username.send_keys(name) 
  password.send_keys(Pass) 
  password.submit()
  for friend in Friends:
   try:
    call(['clear']);blocked.append(friend);print '[+] Blocking: {}\n[+] Blocked {} Friends'.format(str(friend),len(blocked))
    driver2.get("https://www.facebook.com/{}".format(str(friend)))
    driver2.find_element_by_xpath("//button[@class='_42ft _4jy0 _1yzl _p _4jy4 _517h _51sy']").click()
    driver2.find_element_by_xpath("//span[contains(text(), 'Block')]").click();sleep(1.7)
    driver2.find_element_by_xpath("//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']").click()
   except: del blocked[-1];pass
  driver2.quit();return

def Delete_Photos():
 global Photos,Spin2
 call(['clear']);print '[+] Reading Photos\' ID...';sleep(1.7)
 with lock:
  Spin2 = 0
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  driver2 = webdriver.Firefox() 
  driver2.implicitly_wait(1.3)
  driver2.maximize_window() 
  driver2.get("https://www.facebook.com");
  username = driver2.find_element_by_id("email")
  password = driver2.find_element_by_id("pass")
  username.send_keys(name) 
  password.send_keys(Pass) 
  password.submit()
  for photo in Photos:
   try:
    call(['clear']);deleted.append(photo);print '[+] Deleting Photos...\n[+] Deleted Photos: {}'.format(len(deleted))
    driver2.get("https://www.facebook.com/photo.php?fbid={}".format(str(photo)))
    driver2.find_element_by_xpath("//span[contains(text(), 'Options')]").click()
    driver2.find_element_by_xpath("//span[contains(text(), 'Delete This Photo')]").click()
    driver2.find_element_by_xpath("//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']").click()
   except: del deleted[-1];pass
  driver2.quit();return

def Setup():
 global driver
 try: driver =  webdriver.Firefox()
 except: call(['clear']);print'[+] Installing Firefox...';Popen(['sudo','apt-get','install','firefox=45.0.2+build1-0ubuntu1','-y']).wait();Popen(['sudo','apt-mark','hold','firefox']).wait();driver=webdriver.Firefox()
 driver.implicitly_wait(0.3)
 driver.maximize_window() 
 call(['clear']);print '[-] Waiting For Facebook...'
 driver.get('https://www.facebook.com')
		   
def Check_list():
 global Ready
 if not path.exists('/usr/bin/npm'): call(['clear']);print'[+] Installing Npm...';Popen(['sudo','apt-get','install','npm','-y'],stdout=Devnull,stderr=Devnull).wait()
 if not path.exists('/usr/bin/node'): call(['clear']);print'[+] Installing Node.js...';Popen(['sudo','apt-get','install','nodejs-legacy'],stdout=Devnull,stderr=Devnull).wait()     
 if not path.exists('/usr/local/bin/phantomjs'): call(['clear']);print'[+] Installing PhantomJS...';Popen(['sudo','npm','install','-g','phantomjs-prebuilt'],stdout=Devnull,stderr=Devnull).wait()
 if path.exists('/usr/local/selenium/webdriver'): Ready = True
	
if __name__ == '__main__': 
 global Run,Run2,On,On2,Spin,Spin2
 #
 lock = Lock() #Special lock
 # 
 Deleted = []
 deleted = []
 Photos  = []
 Blocked = []
 blocked = []
 Friends = []
 #
 Ready = False
 Run2  = False
 On2   = False
 Run   = True
 On    = True
 Check_list()
 if not Ready: call(['clear']);exit('[!] Please Install Seleium & PhantomJS')
 try:
  call(['clear'])
  name = str(raw_input('Enter Your Facebook [ Username or User ID ]: '))
  Pass = str(raw_input('\nEnter Your Facebook [ Password ]: '))
  Setup()
  Login()	
  Get_Photos = Thread(target=Collect_Photos)
  Get_Friends = Thread(target=Collect_Friends)
  Get_Friends.start();
  Spin = 0;Spin2 = 0
  while Run:
   if len(Friends) != 0:
    Block_Friends()
    del Friends[:];Ran=False;
   else:  call(['clear']);print '[-] Waiting for friends\' list to populate...';sleep(1);Spin+=1
  if not Run: Run2 = True;On2 = True;call(['clear']);print '[-] Photos Time...';Setup();Login();Get_Photos.start()
  while Run2:
   if len(Photos) != 0:
    Delete_Photos()
    del Photos[:];Ran2=False;
   else: call(['clear']);print '[-] Waiting for photos\' list to populate...';sleep(1);Spin2+=1
 except KeyboardInterrupt: On=False;On2=False;Run=False;Run2=False
 finally:
  if not Run and not Run2: call(['clear']);exit('[+] All Done')
