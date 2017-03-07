import os, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from page_login import login

class topic_qs:
	def __init__(self, link, mail, passw, scrolls, save_after):
		self.topic_link = link
		self.user_email = mail
		self.user_passw = passw
		self.scrolls = scrolls
		self.save_after = save_after
		self.scrape_qs()	

	def scrape_qs(self):
		"""
		Arguments:
			example link: "https://www.quora.com/topic/BITS-Pilani-Hyderabad-Campus/all_questions"
			login id and password of user(assuming user is already
			registered on quora and email is verified)
			times to scroll down the end of webpage,
			write to file after every 'save_after' scrolls
		Functioning:
			First sets the chromedriver, signs the user in;
			scrolls to the bottom(number of scrolls limit infinite scrolling);
			gets all the question links;
			saves them in a file and quits.
		"""
		"""
		usage format
		driver.find_elements_by_xpath('//a[starts-with(@class,"more_link")]')

		driver.find_elements_by_xpath('//a[starts-with(@class,"question_link")]')

		driver.find_elements_by_xpath('//*[starts-with(@*,"*") and contains(@*,"*")]')
		"""

		# installation tip!
		# https://chromedriver.storage.googleapis.com/index.html?path=2.27/
		# download from ^, copy it to /usr/bin/ and give it executable permissions(a+x)
		chromedriver = "/usr/bin/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		
		#PhantomJS
		#https://bbuseruploads.s3.amazonaws.com/fd96ed93-2b32-46a7-9d2b-ecbc0988516a/downloads/396e7977-71fd-4592-8723-495ca4cfa7cc/phantomjs-2.1.1-linux-x86_64.tar.bz2?Signature=JRuhEe3%2Bn4Hm8QgXoWq0vuuDDYo%3D&Expires=1488867854&AWSAccessKeyId=AKIAIVFPT2YJYYZY3H4A&versionId=null&response-content-disposition=attachment%3B%20filename%3D%22phantomjs-2.1.1-linux-x86_64.tar.bz2%22
		#self.driver = webdriver.PhantomJS()
		
		self.driver.get(self.topic_link)
		
		login(self.user_email, self.user_passw, self.driver)

		#setting the filename to be saved
		if (self.topic_link.endswith('/all_questions') or self.topic_link.endswith('/all_questions/')):
			self.filename = self.topic_link[28:-14]
		else:
			if self.topic_link.endswith('/'):
				self.filename = self.topic_link[28:-1]
			else:
				self.filename = self.topic_link[28:]
		self.filename = '../database/question_links/' + self.filename + ".txt"

		self.counter=0
		self.questions_extrated=0
		self.completed_list=[]
		self.total = self.scrolls
		try:
			with open (self.filename,"r") as f:
				self.completed_list=f.readlines()
		except:
			self.completed_list=[]
		
		for i in range(0,self.scrolls):
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			
			self.counter = self.counter + 1
			
			try:
				#clicking more button that may sometimes appear during infinite scrolling
				self.more_class = self.driver.find_elements_by_class_name("PagedListMoreButton")[0]
				self.more_button = self.more_class.find_elements_by_xpath('//div[contains(text(),"More")]')[0]
				self.more_button.click()
				time.sleep(.2)
			except:
				#code comes here if more button doesn't appear
				time.sleep(.2)
		
			if self.counter == self.save_after:
				#getting all the question links	
				self.question_links = self.driver.find_elements_by_xpath('//a[starts-with(@class,"question_link")]')
				#writing to a file if it is not already there
				with open (self.filename,"a") as f:
					for a_link in self.question_links:
						if a_link.get_attribute('href')+'\n' not in self.completed_list:
							if not a_link.get_attribute('href').startswith("https://www.quora.com/unanswered"):
								print(a_link.get_attribute('href'))
								f.write(a_link.get_attribute('href')+'\n')
								self.questions_extrated = self.questions_extrated+1
								self.completed_list.append(a_link.get_attribute('href')+'\n')
					f.close()
				self.counter = 0
				self.total -= self.save_after
				print("[total] "+str(self.questions_extrated)+" unique questions extracted... [scrolls rem.:"+str(self.total)+"]")
		
		self.driver.close()

#t = topic_qs("https://www.quora.com/topic/BITSAT-BITS-Admission-Test/all_questions","thebitsatbot@gmail.com", " Use at least 8 characters.", 500, 10)