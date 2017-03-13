import questions_link_extractor as qle
import answers_extractor as ae

page_links = ["https://www.quora.com/topic/BITSAT-BITS-Admission-Test/all_questions",
"https://www.quora.com/topic/BITSAT-Preparation/all_questions",
"https://www.quora.com/topic/Birla-Institute-of-Technology-and-Science-Pilani-1/all_questions",
"https://www.quora.com/topic/Life-at-BITS-Pilani-Pilani-Campus-1/all_questions",
"https://www.quora.com/topic/BITS-Pilani-K-K-Birla-Goa-Campus-4/all_questions",
"https://www.quora.com/topic/Birla-Institute-of-Technology-and-Science-Pilani-Pilani-Campus/all_questions",
"https://www.quora.com/topic/BITS-Pilani-Hyderabad-Campus/all_questions",
"https://www.quora.com/topic/BITS-Alumni-Association-1/all_questions",
"https://www.quora.com/topic/Birla-Institute-of-Technology-Science-Pilani-Dubai-Campus/all_questions"]
single_link = page_links[1]
mail = "thebitsatbot@gmail.com"
passw = " Use at least 8 characters."

def scrape_multiple_topics(page_links, mail, passw, scrolls=100, save_after=10):
	"""
	scrapes the links of questions in the topics in the list
	not advisable if no of questions in topics is large
	"""
	for page_link in page_links:
		qle.topic_qs(page_link, mail, passw, scrolls, save_after)


def scrape_single_topic(link, mail, passw, scrolls=100, save_after=10):
	"""
	scrapes the links of questions in a topic
	"""
	qle.topic_qs(link, mail, passw, scrolls, save_after)


def scrape_answers(topic_link, max_ans=10, max_scrolls=50):
	"""
	assuming questions file already exist

	"""
	#setting up the filenames
	if (topic_link.endswith('/all_questions') or topic_link.endswith('/all_questions/')):
			filename = topic_link[28:-14]
	else:
		if topic_link.endswith('/'):
			filename = topic_link[28:-1]
		else:
			filename = topic_link[28:]
	filenameJSON = '../database/main_data/' + filename + ".json"
	filenameText = '../database/question_links/' + filename + ".txt"
	
	with open (filenameText,'r') as f:
		questions = f.readlines()
	
	count = len(questions)
	for question in questions:
		#since '\n' is at the end of every question
		ae.q_link(question[:-1], filenameJSON, max_ans, max_scrolls)
		count-=1
		print("[remaining] "+str(count)+" questions to be scraped")

#scrape_multiple_topics(page_links, mail, passw, 1000, 10)
#scrape_single_topic(single_link, mail, passw, 3500, 10)
scrape_answers(single_link,  3, 2)
