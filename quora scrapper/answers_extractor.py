import requests
from bs4 import BeautifulSoup

question_url = "https://www.quora.com/How-do-I-study-Inorganic-Chemistry-for-JEE-16-Mains+Advanced-and-BITSAT"

req = requests.get(question_url)
soup = BeautifulSoup(req.content, "lxml")

answer_panel = soup.find("div",{
	"class": "AnswerPagedList"
	})

all_answers = answer_panel.find_all("div", {
	"class": ["AnswerBase", "Answer"]
	}, limit=6)

for ans in all_answers:
	print ans.text