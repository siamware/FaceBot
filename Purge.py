#!/usr/bin/env python2.7
#
# Blocks Friends For You, Good For Cleaning Up Old Facebook Accounts
#
# Designed For Kali Linux 2.0, But Might Work For Ubuntu
#
from re import search
from time import sleep
from Queue import Queue
from sys import exit,argv
from subprocess import call,Popen
from threading import Thread,Lock
from datetime import datetime as Time
from os import path,getuid,devnull,remove
#
Devnull = open(devnull, 'w')
if getuid() != 0: call('clear');exit('[!] Please run this program with root access\n\nEx: sudo python {}'.format(argv[0]))
if not path.exists('/usr/bin/pip'): call(['clear']);print '[+] Installing Python-pip...';Popen(['sudo','apt-get','install','python-pip','-y'],stdout=Devnull,stderr=Devnull).wait()
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
  if Friends.qsize() == 0:#if len(Friends) == 0:
   with lock:
    if Spin >= 20: driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");Spin=0
    Elems = driver.find_elements_by_xpath("//a[@href][@tabindex='-1'][@aria-hidden='true']")
    for elem in Elems: 
     if Ran == False: Ran = True
     Link = str(elem.get_attribute("href"))
     
     if search('friends_tab',Link): 
      Id = []
      for p,i in enumerate(Link):
       if p >= 40 and p <=54: Id.append(i)
      tmp_Id =  ''.join(Id)
      if tmp_Id.isalnum(): Friends.put(tmp_Id);continue
      x=0
      Starts = 25
      for l in Link: 
       if l.strip() == str('?').strip() : End = int(x);break
       x+=1
      friend = str(Link[Starts:End]).strip()
      if friend == 'profile.php'.strip(): continue
      Friends.put(friend);continue
    if Friends.qsize() == 0 and Ran: driver.quit();Run = False;On=False
			  
def Login():
 call(['clear']);print '[-] Login In Progress...'
 username = driver.find_element_by_id("email")
 password = driver.find_element_by_id("pass")
 username.send_keys(name)
 password.send_keys(Pass) 
 password.submit()
 CurrentUrl = str(driver.current_url).strip()
 if CurrentUrl != 'https://www.facebook.com/'.strip(): driver.quit();exit('[+] Incorrect Logins')

def Current_time():
 current = str(Time.today())[11:16]
 time = Time.strptime('{}'.format(current),'%H:%M')
 now_time = time.strftime('%I:%M %p')
 return now_time

def Delete_Conversations():
 global driver
 driver =  webdriver.Firefox()
 driver.implicitly_wait(0.3)
 driver.maximize_window() 
 call(['clear']);print '[-] Waiting For Facebook...'
 driver.get('https://www.facebook.com')
 Login()
 call(['clear']);print'[+] Deleting Messages'
 for i in range(20): #Because it will take forever to delete all
  driver.get('www.facebook.com/messages')
  try:driver.find_element_by_xpath("//*[@class='_42ft _4jy0 _2cna _p _4jy3 _517h _51sy']").click()
  except:break
  driver.find_element_by_xpath("//*[contains(text(),'Delete Conversation...')]").click()
  driver.find_element_by_xpath("//*[@class=' layerCancel _4jy0 _4jy3 _4jy1 _51sy selected _42ft']").click()
 #----------#  
 driver.quit()
	
def Block_Friends():
 global Friends,Spin,blocked,driver2
 
 with lock:
  try: remove('ghostdriver.log')
  except: pass
  call(['clear']);print '[+] Reading Friends list...';sleep(1.7)
  Spin = 0
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  driver2 =  webdriver.Firefox()
  driver2.implicitly_wait(1.3)
  driver2.maximize_window() 
  call(['clear']);print '[+] Waitinq For Facebook...'
  driver2.get("https://www.facebook.com");
  username = driver2.find_element_by_id("email")
  password = driver2.find_element_by_id("pass")
  username.send_keys(name) 
  password.send_keys(Pass) 
  password.submit()
  while not Friends.empty():
   friend = Friends.get()
   call(['clear']);blocked+=1;print '[+] Blocking: {}\n[+] Blocked {} Friends'.format(str(friend),blocked)
   if friend.isalnum(): Method_2(friend);continue
   try:Method_1(friend)
   except: 
    try: Method_2(friend) 
    except: blocked-=1

  while 1: 
   try: driver.get(driver.current_url);break #Refresh Friends list Page
   except: pass

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  driver2.quit();return

def Method_2(friend):
 global driver2
 driver2.get("https://www.facebook.com/{}".format(str(friend)))
 driver2.find_element_by_xpath("//button[@class='_42ft _4jy0 _1yzl _p _4jy4 _517h _51sy']").click()
 driver2.find_element_by_xpath("//span[contains(text(), 'Block')]").click();sleep(1.7)
 driver2.find_element_by_xpath("//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']").click()
   
def Method_1(friend):
    global driver2
    driver2.get("https://www.facebook.com/settings?tab=blocking")
    driver2.find_element_by_xpath(".//*[@class='inputtext mrm _iw2']").send_keys(friend);sleep(1.7)
    driver2.find_element_by_xpath(".//*[@class='uiButton uiButtonConfirm']").click();sleep(0.7)
    driver2.find_element_by_xpath(".//*[@class='mrm uiButton']").click();sleep(0.3)
    driver2.find_element_by_xpath(".//button[@class='_42ft _42fu layerConfirm uiOverlayButton selected _42g- _42gy']").click()
    
def Finish_Up():
 call(['clear']);print'[+] Cleaning Up...';sleep(3)
 while 1:
  try: Setup();break
  except: pass
 while 1: 
  try: Login();break
  except: pass
 while 1: 
  try: driver.get("https://www.facebook.com/settings?tab=security&section=sessions&view");break
  except: pass
 while 1:
  try: driver.find_element_by_xpath("//a[contains(text(),'End All Activity')]").click();break
  except: pass
 driver.quit()
 
  

def Setup():
 global driver
 try: driver =  webdriver.PhantomJS()
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
 global Run,On,Spin
 #
 lock = Lock() #Special lock
 # 
 Friends = Queue()
 blocked = 0
 #
 Ready = False
 Run   = True
 On    = True
 Check_list()

 if not Ready: call(['clear']);exit('[!] Please Install Seleium & PhantomJS')
 try:
  call(['clear'])
  name = str(raw_input('Enter Your Facebook [ Username or User ID ]: '))
  Pass = str(raw_input('\nEnter Your Facebook [ Password ]: '))
  call(['clear']);print'[+] When To Start?';sleep(1.3)
  Msg = 'Enter As: HH:MM'
  call(['clear']);print Msg
  hr = raw_input('Enter hour: ')
  call(['clear']);print Msg
  mins = raw_input('Enter Minutes: ')
  formats = raw_input('Enter am|pm: ').upper()
  Convert1 = Time.strptime('{}:{}'.format(hr,mins),'%H:%M')
  Convert2 = Convert1.strftime('%I:%M')
  hr = str(Convert2)[0:2]
  mins = str(Convert2)[3:6]
  while 1:
   try:
    Current_time()
    now_hrs  = str(Current_time())[0:2]
    now_mins = str(Current_time())[3:6]
    now_form = str(Current_time())[6:8]
    if int(now_hrs) == int(hr) and int(now_mins) == int(mins) and now_form == formats: break
    else: 
     try:call(['clear']);print '[+] Waitinq Til:  {} {}\n[+] Current Time: {}'.format(Convert2,formats,Current_time());sleep(0.5)
     except: call(['clear']);break
   except: call(['clear']);break
  Setup()
  Login()	
  Get_Friends = Thread(target=Collect_Friends)
  Get_Friends.start();
  Spin = 0
  while Run:
   if Friends.qsize() != 0:
    Block_Friends();
    Ran=False;
   else:  call(['clear']);print '[-] Waiting For Friend List To Populate...';sleep(1);Spin+=1
 except KeyboardInterrupt: On=False;Run=False
 finally:
  if not Run:  
    try: remove('ghostdriver.log')
    except: pass
    finally: 
     Delete_Conversations()
     if blocked != 0: Finish_Up();
     call(['clear']);exit('[+] All Done')
