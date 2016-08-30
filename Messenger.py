#!/usr/bin/env python
#
# Adds Friends For You
#
# Designed For Kali Linux 2.0 
#
from re import search
from time import sleep
from sys import exit,argv
from random import choice
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
	driver.get("https://www.facebook.com/{}/friends?source_ref=pb_friends_tl".format(str(Vic)))
	Ran = False
	while On:
	    if len(Friends) == 0:
		with lock:
		 if Spin >= 20: driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");Spin=0
		 elems = driver.find_elements_by_xpath(".//a[@div='u_0_38']")
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

		   if not search(friend,str(ADDED)) and friend != 'profile.php'.strip(): 
			 
			 Friends.append(friend);ADDED.append(friend);
			

		 if len(Friends) == 0 and Ran: driver.quit();Run = False;On=False
		  
	 
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
	
def Add_Friends():
	global Friends,Spin
	call(['clear']);print '[+] Reading list...';sleep(1.7)
	with lock:
	 Spin = 0
	 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"); #Scroll Down On The Friendlist

	 driver2 = webdriver.Firefox()#Open New Window for Adding
	 driver2.implicitly_wait(1.3)
	 driver2.maximize_window() 
	 driver2.get("https://www.facebook.com");
	 username = driver2.find_element_by_id("email")
	 password = driver2.find_element_by_id("pass")
	 username.send_keys(name) #Login
	 password.send_keys(Pass) 
	 password.submit()
	
	 for friend in Friends: 
	   wait = choice([1,2,3,4,5,6,7,8,9,10])
           try:
	    call(['clear']);added.append(friend);print '[+] Sending Message To: {}\n[+] Sent To {} People'.format(str(friend),len(added))
	    driver2.get("https://www.facebook.com/{}".format(str(friend)))
	    driver2.find_element_by_xpath("//*[@class='_42ft _4jy0 _4jy4 _517h _51sy']").click()
	    Box = driver2.find_element_by_xpath("//*[@class='_5rpu']");Box.send_keys(Message);Box.send_keys(Keys.ENTER)
	    driver2.find_element_by_xpath("//*[@class='_3olu _3olv close button']").click();sleep(wait)
           except: del added[-1];sleep(wait)
	 driver2.quit();return
	 
def Check_list():
 global Ready
 if not path.exists('/usr/bin/npm'): call(['clear']);print'[+] Installing Npm...';Popen(['sudo','apt-get','install','npm','-y'],stdout=Devnull,stderr=Devnull).wait()
 if not path.exists('/usr/bin/node'): call(['clear']);print'[+] Installing Node.js...';Popen(['sudo','apt-get','install','nodejs-legacy'],stdout=Devnull,stderr=Devnull).wait()     
 if not path.exists('/usr/local/bin/phantomjs'): call(['clear']);print'[+] Installing PhantomJS...';Popen(['sudo','npm','install','-g','phantomjs-prebuilt'],stdout=Devnull,stderr=Devnull).wait()
 if path.exists('/usr/local/selenium/webdriver'): Ready = True	

if __name__ == '__main__': 
	global driver,Run,On,Spin
	lock = Lock()
	ADDED = []
	added = []
	Friends = []
	Ready = False
	Run = True
	On = True
	Check_list()
 	if not Ready: call(['clear']);exit('[!] Please Install Seleium & PhantomJS')
	try:
		call(['clear'])
		name = str(raw_input('Enter Your Username | User ID: '))
		Pass = str(raw_input('\nEnter Your  Password: '))
		Vic  = str(raw_input('\n\nEnter Target Username | User ID: '));sleep(0.7);call(['clear'])
		Message = str(raw_input("Enter Your Message Below\n\n"))
		if len(Message) == 0: call(['clear']);exit('[!] You Must A Message')

	
		driver = webdriver.Firefox()
		driver.implicitly_wait(3)
		driver.maximize_window() 
		call(['clear']);print '[-] Waiting For Facebook...'
		driver.get('https://www.facebook.com')
		Login()

		Get_Friends = Thread(target=Collect_Friends)
	
		Get_Friends.start();
		Spin = 0
		while Run:
		   if len(Friends) != 0:
			Add_Friends()
			del Friends[:];Ran=False;

		   else:
			call(['clear']);print '[-] Waiting for list to populate...';sleep(1)
			Spin+=1
	
	except KeyboardInterrupt: On=False;Run=False;
	finally: 
	 if not Run: call(['clear']);exit('[+] All Done')
