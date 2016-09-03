#!/usr/bin/env python2.7
#
# Like all of your friends facebook photos
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
if not path.exists('/usr/bin/pip'): call(['clear']);print '[+] Installing Python-pip...';Popen(['sudo','apt-get','install','python-pip','-y'],stdout=Devnull,stderr=Devnull).wait())
try: from selenium import webdriver;from selenium.webdriver.common.keys import Keys
except: call(['clear']);print'[+] Installing Selenium...';Popen(['sudo','pip','install','-U','selenium'],stdout=Devnull,stderr=Devnull).wait()
try: from selenium import webdriver;from selenium.webdriver.common.keys import Keys
except ImportError: call(['clear']);exit('[!] Need Selenium & PhantomJS To Run...') 
#


def Collect_Photos():
	global On,Run
	driver.get('https://www.facebook.com/{}/photos_all'.format(str(target)))
	Ran = False
	while On:
	 if len(Photos) == 0:
          with lock:
		  elems = driver.find_elements_by_xpath("//a[@href]")
		  for elem in elems: 
			Link = str(elem.get_attribute("href"));
			if Ran == False: Ran = True
			if 'photo.php' in Link or search('photo.php',Link): 
					x=0
					Starts = 40
					for l in Link: x+=1
					End = int(x)
					photo = str(Link[Starts:End]).strip();
			
					if photo not in Liked:
					 Photos.append(photo);Liked.append(photo)
		  if len(Photos) == 0 and Ran: driver.quit();Run = False;On=False

def Setup():
	global driver
	driver = webdriver.Firefox()
	driver.implicitly_wait(0.3)
	driver.maximize_window() 
	call(['clear']);print '[-] Waiting For Facebook...';sleep(2)
	driver.get('https://www.facebook.com')

def Login():
	call(['clear']);print '[-] Login In Progress...';sleep(1.7)
	username = driver.find_element_by_id("email")
	password = driver.find_element_by_id("pass")
	username.send_keys(User)
	password.send_keys(passwrd) 
	call(['clear'])
	password.submit()
	CurrentUrl = str(driver.current_url).strip()
	if CurrentUrl != 'https://www.facebook.com/'.strip(): driver.quit();exit('[+] Incorrect Logins')
	

def Like_Photos():
	global Photos
	with lock:
	  Spin=0;call(['clear']);print '[+] Reading Photos\' ID...';sleep(1.7)
	  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	  try: driver2 = webdriver.Firefox() 
	  except: driver2 = webdriver.Firefox()
	  driver2.implicitly_wait(3)
	  driver2.maximize_window()
	  driver2.get("https://www.facebook.com");
	  username = driver2.find_element_by_id("email")
	  password = driver2.find_element_by_id("pass")
	  username.send_keys(User) 
	  password.send_keys(passwrd) 
	  password.submit()
	  for photos in Photos:
	   call(['clear']);print '[+] Liking Photos...'
	   driver2.get('https://www.facebook.com/photo.php?fbid={}'.format(str(photos)))
	   try:
	    driver2.find_element_by_xpath(".//*[@id='fbPhotoSnowliftFeedback']/div/div[1]/div/div/div/div/span[1]/div/a").click()
	   except: pass
	  del Photos[:];Ran=False;driver2.quit()

def Check_list():
 global Ready
 if not path.exists('/usr/bin/npm'): call(['clear']);print'[+] Installing Npm...';Popen(['sudo','apt-get','install','npm','-y'],stdout=Devnull,stderr=Devnull).wait()
 if not path.exists('/usr/bin/node'): call(['clear']);print'[+] Installing Node.js...';Popen(['sudo','apt-get','install','nodejs-legacy'],stdout=Devnull,stderr=Devnull).wait()     
 if not path.exists('/usr/local/bin/phantomjs'): call(['clear']);print'[+] Installing PhantomJS...';Popen(['sudo','npm','install','-g','phantomjs-prebuilt'],stdout=Devnull,stderr=Devnull).wait()
 if path.exists('/usr/local/selenium/webdriver'): Ready = True

if __name__ == '__main__':
	global Spin;Spin = 0
	lock = Lock()
	Ready = False
	Ran = False
	Run = True
	On = True
	Photos = []
	Liked  = []
	Check_list()
 	if not Ready: call(['clear']);exit('[!] Please Install Seleium & PhantomJS')
 
	#
	try:
		call(['clear']);User = str(raw_input("Enter Your Username: "))
		passwrd = str(raw_input('\nEnter Your Password: '))
		target = str(raw_input('\n\nEnter Your Target\'s Username: '));sleep(0.7);call(['clear'])
		Setup();Login()
		Thread(target=Collect_Photos).start()
		while Run:
		    if len(Photos) != 0:
		       Like_Photos()
		       del Photos[:]
		    else:
			pass
			#call(['clear']);
			#print '[-] Waiting for photos\' list to populate...';sleep(1);Spin+=1
	except KeyboardInterrupt: Run = False;On=False
	call(['clear']);exit('[+] All Done')
