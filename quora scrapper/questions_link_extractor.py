import os, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class topic_qs:
	def login_and_scrape(self,link, mail, passw, scrolls):
		"""
		Arguments:
			example link: "https://www.quora.com/topic/BITS-Pilani-Hyderabad-Campus/all_questions"
			takes topic link to extract, login id of user(assuming user is already
			registered on quora and email is verified), password of user, times to
			scroll the webpage
		Functioning:
			First sets the chromedriver, signs the user in;
			scrolls to the bottom(number of scrolls limit infinite scrolling);
			gets all the question links;
			saves them in a file and quits.
		"""

		self.topic_link = link
		self.user_email = mail
		self.user_passw = passw
		self.scrolls = scrolls
		
		# installation tip!
		# https://chromedriver.storage.googleapis.com/index.html?path=2.27/
		# download from ^, copy it to /usr/bin/ and give it executable permissions(a+x)
		chromedriver = "/usr/bin/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)

		self.driver.get(self.topic_link)

		"""
		usage format
		driver.find_elements_by_xpath('//a[starts-with(@class,"more_link")]')

		driver.find_elements_by_xpath('//a[starts-with(@class,"question_link")]')

		driver.find_elements_by_xpath('//*[starts-with(@*,"*") and contains(@*,"*")]')
		"""

		self.driver.find_elements_by_xpath('//div[contains(text(), "Sign In")]')[0].click()
		time.sleep(0.8)
		self.driver.find_elements_by_xpath('//a[contains(text(), "I Have a Quora Account")]')[0].click()
		time.sleep(0.5)

		#tip! :: if you are using login from Quora home page use regular_login instead of normal_login
		#signing in through topic page
		self.login_class=self.driver.find_elements_by_class_name('normal_login')

		self.email=self.login_class[0].find_element_by_name('email')
		self.email.send_keys(self.user_email)

		self.password=self.login_class[0].find_element_by_name('password')
		self.password.send_keys(self.user_passw)

		time.sleep(0.5)
		self.login_class[0].find_elements_by_class_name('submit_button')[0].click()
		time.sleep(2)


		for i in range(0,self.scrolls):
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			try:
				#clicking more button that may sometimes appear during infinite scrolling
				self.more_class = self.driver.find_elements_by_class_name("PagedListMoreButton")[0]
				self.more_button = self.more_class.find_elements_by_xpath('//div[contains(text(),"More")]')[0]
				self.more_button.click()
				time.sleep(.2)
			except:
				#code comes here if more button doesn't appear
				time.sleep(.2)
		
		#getting all the question links	
		self.question_links = self.driver.find_elements_by_xpath('//a[starts-with(@class,"question_link")]')

		#setting the filename to be saved
		if (self.topic_link.endswith('/all_questions') or self.topic_link.endswith('/all_questions/')):
			self.filename = self.topic_link[28:-14]
		else:
			if self.topic_link.endswith('/'):
				self.filename = self.topic_link[28:-1]
			else:
				self.filename = self.topic_link[28:]
		self.filename = './database/question_links/' + self.filename 

		#writing to a file if it is not already there
		self.questions_extrated=0
		self.completed_list=[]
		with open (self.filename,"w") as f:
			for a_link in self.question_links:
				if a_link.get_attribute('href') not in self.completed_list:
					f.write(a_link.get_attribute('href')+'\n')
					self.questions_extrated = self.questions_extrated+1
					self.completed_list.append(a_link.get_attribute('href'))

		print(self.questions_extrated)
		driver.close()

t = topic_qs()
t.login_and_scrape("__topic_link_here__","__email_id_here__", "__enter_your_password_here__", no. of scrolls here)