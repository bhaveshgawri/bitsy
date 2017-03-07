import os, time, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from page_login import login


class q_link:
	def scrape_details(self, question_url, mail, passw, max_ans=4, max_scrolls=250):

		self.q_url = question_url
		self.user_email = mail
		self.user_passw = passw
		self.max_limit = max_ans
		self.max_scrolls = max_scrolls
		#q_url = "https://www.quora.com/How-do-I-study-Inorganic-Chemistry-for-JEE-16-Mains+Advanced-and-BITSAT"

		chromedriver = "/usr/bin/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.get(self.q_url)

		login(self.user_email, self.user_passw, self.driver)

		if self.max_limit <= 5:
			self.scrolls = 50
		elif self.max_limit > 5 and self.max_limit < 10:
			self.scrolls = 80
		else:
			self.scrolls = self.max_scrolls
		
		for i in range(0,self.scrolls):
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(0.2)

		req = requests.get(question_url)
		self.soup = BeautifulSoup(req.content, "lxml")

		answer_panel = soup.find("div",{
			"class": "AnswerPagedList"
			})

		all_answers = answer_panel.find_all("div", {
			"class": ["AnswerBase", "Answer"]
			}, limit=self.max_limit)

		for ans in all_answers:
			print ans.text

t = q_link()
t.scrape_details("https://www.quora.com/topic/BITSAT-BITS-Admission-Test/all_questions","thebitsatbot@gmail.com", " Use at least 8 characters.", 500, 10)
#t.login_and_scrape('url','email','passw',scrolls, save_after_scrolls)