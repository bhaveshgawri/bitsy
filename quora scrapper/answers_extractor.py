import os, time, json, requests, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class q_link:
	def scrape_details(self, database, question_url, max_ans=10, max_scrolls=100):

		self.q_url = question_url
		self.max_limit = max_ans
		self.max_scrolls = max_scrolls

		chromedriver = "/usr/bin/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.get(self.q_url)

		if self.max_limit <= 5:
			self.scrolls = 25
		elif self.max_limit > 5 and self.max_limit < 10:
			self.scrolls = 45
		else:
			self.scrolls = self.max_scrolls
		
		for i in range(0,self.scrolls):
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(0.2)

		req = requests.get(question_url)
		self.soup = BeautifulSoup(req.content, "lxml")

		self.answer_panel = self.soup.find("div",{
			"class": "AnswerPagedList"
			})

		self.all_answers = self.answer_panel.find_all("div", {
			"class": ["AnswerBase", "Answer"]
			}, limit=self.max_limit)

			
		answer_set=[]
		for answer in self.all_answers:
			ans_box = answer.find_all("div",{
				"class": ["ExpandedQText", "ExpandedAnswer"]
				})
			full_ans = ans_box[0].find("span",{
				"class": "rendered_qtext"
				})
			ans=[]
			for ans_part in full_ans:
				if ans_part.name is 'p':
					ans.append(ans_part.get_text())
					try:
						ans_links = ans_part.find_all('a')
						for ans_link in ans_links:
							if ans_link.get('href').startswith('/profile/'):
								ans.append(ans_link.get_text()+" @ https://quora.com"+ans_link.get('href'))
							else:
								ans.append(ans_link.get_text()+" @ "+ans_link.get('href'))
					except:
						ans.append(ans_part.get_text())
				elif ans_part.name is 'div':
					images=ans_part.find_all('img',{
						"class": ['qtext_image_placeholder', 'landscape', 'qtext_image', 'zoomable_in', 'zoomable_in_feed']
						})
					for img in images:
						ans.append(img.get('src'))
				
			#print(ans)
			answer_set.append(ans)
		
		database[self.q_url] = answer_set
		file = open('data.json','w')
		json.dump(database, file)
		file.close
		return database

database={}
t = q_link()
database = t.scrape_details(database, "https://www.quora.com/Why-did-NASA-extend-Hubbles-lifetime-by-another-five-years", 2, 2)