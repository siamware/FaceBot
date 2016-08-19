#!/usr/bin/env python
# 
# When You Want To Clean Out Your Old Account, But You're Too Lazy To Do It Manually, Deletes Most, But Not All.
# 
# 
# Warning: This Program Can/Will Damage Your Account If Used Incorrectly, Only Use It When You Need To Clean Out Your Old Facebook Account.
#
# Educational Purposes Only
#

from re import search
from time import sleep
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

 
def Collect_Friends():
	driver.get("https://www.facebook.com/{}/friends?source_ref=pb_friends_tl".format(str(name)))
	call(['clear']);print'[+] Collecting {}\'s Friends...'.format(name);sleep(0.7)
	elems = driver.find_elements_by_xpath("//a[@href]")
	for elem in elems: 
    		try:
			Link = str(elem.get_attribute("href"))
			
			if 'friends_tab' in Link or search('friends_tab',Link): 
				x=0
				Starts = 25
				for l in Link: 
					if l.strip() == str('?').strip() : End = int(x);break
					x+=1
				friend = Link[Starts:End]
				if str(friend).strip() not in Friends and str(friend).strip() != 'profile.php'.strip():
				 Friends.append(str(friend).strip())

		except:pass

def Block_Friends():
	Blocked=0
	call(['clear']);print '[+] Found {} Friends In Friends list'.format(len(Friends));sleep(1);
	

	for friend in Friends:
		try:
		 Blocked+=1;call(['clear']);print '[+] Blocking: {}\n[+] Remaining Friends: {}'.format(str(friend),str( len(Friends)-Blocked));	 


		 driver.get("https://www.facebook.com/{}".format(str(friend)))
		 drop = "//button[@class='_42ft _4jy0 _1yzl _p _4jy4 _517h _51sy']"
		 driver.find_element_by_xpath(drop).click()

		 value = 'Block'
		 span_xpath = '//span[contains(text(), "' + value + '")]'
		 span_element = driver.find_element_by_xpath(span_xpath).click()

		 Block = "//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']"
		 driver.find_element_by_xpath(Block).click()
		except: pass


def Delete_Photos():		
	Deleted=0
	call(['clear']);print '[+] Found {} Photos'.format(len(Photos));sleep(1.3)
	for pic in Photos:
		try:
		 Deleted+=1;call(['clear']);print '[+] Remaining Photos: {}'.format(str( len(Photos)-Deleted));
		 driver.get('https://www.facebook.com/photo.php?fbid={}'.format(str(pic)));sleep(1.7)
		 value2 = 'Delete This Photo'
		 value = 'Options'
		
	
		 span_xpath = '//span[contains(text(), "' + value + '")]'
		 span_xpath2 = '//span[contains(text(), "' + value2 + '")]'

		 span_element = driver.find_element_by_xpath(span_xpath).click()
		 span_element = driver.find_element_by_xpath(span_xpath2).click()
		
		 DeleteButton = "//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']"
		 driver.find_element_by_xpath(DeleteButton).click()
		except: pass
	
		

def Collect_Photos(site):
	driver.get(site)
	call(['clear']);print '[+] Collecting {}\'s Photo'.format(str(name))
	elems = driver.find_elements_by_xpath("//a[@href]")
	for elem in elems: 
    		try:
			Link = str(elem.get_attribute("href"))
			
			if 'photo.php' in Link or search('photo.php',Link): 
				x=0
				Starts = 40
				for l in Link: x+=1
				End = int(x)
				photo = Link[Starts:End];
				
				if str(photo).strip() not in Photos:
				 Photos.append(str(photo).strip())

		except:pass

def Facebook():
	driver.get("https://www.facebook.com")

def End_Sessions():
	call(['clear']);print '[+] Disconnecting {} From All Phones'.format(str(name))
	driver.get('https://www.facebook.com/settings?tab=security&section=sessions&view')
	value = 'End All Activity'
	span_xpath = '//a[contains(text(), "' + value + '")]'
	span_element = driver.find_element_by_xpath(span_xpath).click()



def Login():
	username = driver.find_element_by_id("email")
	password = driver.find_element_by_id("pass")

	username.send_keys(name)
	password.send_keys(Pass) 
	password.submit()
	
	CurrentUrl = str(driver.current_url).strip()
	if CurrentUrl != 'https://www.facebook.com/'.strip(): driver.quit();call(['clear']);exit('[+] Incorrect Logins')
	

	

def Setup():
	global driver
	driver = webdriver.Firefox()
	driver.implicitly_wait(0.3)
	driver.maximize_window()



if __name__ == '__main__':
	Photos = []
	Friends = []
	call(['clear'])
	name = str(raw_input('Enter Username | User ID: '))
	Pass = str(raw_input('\nEnter Password: '))
	
	photolink1 = 'https://www.facebook.com/{}/photos_all'.format(str(name))
	photolink2 = 'https://www.facebook.com/{}/photos?source_ref=pb_friends_tl'.format(str(name))

	call(['clear'])
	Setup();Facebook();Login();sleep(1.5);
	Collect_Friends();Collect_Photos(photolink1);Collect_Photos(photolink2)
 	Block_Friends()
	Delete_Photos()
	End_Sessions()
	driver.quit()
	call(['clear']);print '[+] All Done'
