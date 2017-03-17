import json
from difflib import SequenceMatcher as sm
from operator import itemgetter
from os import listdir
from os.path import isfile
from format_chatbot_input import format_

class Q_n_A:
	def __init__(self, asked_question):
		self.asked_question = asked_question
		self.path = "../database/formatted_questions/"
		self.ans_path = "../database/main_data/"
		self.possible_questions=[]
		self.highest_probability_questions=[]
		self.best_question=()
		self.find_best_Qs()
		self.filter_best_Qs()
		self.find_answer()

	def find_best_Qs(self):
		
		filtered_bot_question = format_(self.asked_question)

		filelist = [file for file in listdir(self.path) if isfile(self.path + file)]

		for file in filelist:
			file = self.path+file
			with open (file, "r"):
				database = json.load(open(file))

			ratiolist=[]
			for question, formatted_question in database.items():
				matcher = sm(None, filtered_bot_question, formatted_question)		
				#ratiolist has tuple of question whose probability of matching the
				#question from bot is max when compared with formated_question(its 
				#formated version) in the specific json file
				ratiolist.append((question, matcher.ratio(), file))
			
			#max according to probability
			max_tuple = max(ratiolist, key=itemgetter(1))
			max_prob = max_tuple[1]
			
			for tuple_ in ratiolist:
				if tuple_[1]==max_prob:
					self.possible_questions.append((tuple_[0], tuple_[1], tuple_[2]))

		#print(self.possible_questions)

	def filter_best_Qs(self):
		max_tuple = max(self.possible_questions, key=itemgetter(1))
		max_prob = max_tuple[1]
		temp_max_prob_list = []
		for tuple_ in self.possible_questions:
			if tuple_[1]==max_prob:
				temp_max_prob_list.append((tuple_[0], tuple_[1], tuple_[2], len(tuple_[0]) ))
		
		#finding the question with max length
		#since the match probablity is same question, most similar is question with max length
		#can also choose MIN (v) in below statement because shortest q would be most general
		max_tuple = max(temp_max_prob_list, key=itemgetter(3))
		max_len = max_tuple[3]
		for tuple_ in temp_max_prob_list:
			if tuple_[3]==max_len:
				self.highest_probability_questions.append((tuple_[0], tuple_[1], tuple_[2]))

		#picking the first question from list of max len and highest prob
		self.best_question =  self.highest_probability_questions[0]
		#print(self.best_question)
		
	def find_answer(self):
		file_to_open = self.ans_path + self.best_question[2][len(self.path):]
		with open (file_to_open, "r"):
			database = json.load(open(file_to_open))	
		Q_to_search = "https://www.quora.com/" + self.best_question[0]

		for ques, ans in database.items():
			if ques == Q_to_search:
				for ans_part in ans[0]:
					print(ans_part)


new_question = "Is there a scholarship at BITS"
qna = Q_n_A(new_question)