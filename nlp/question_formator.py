#import xyz library
import io, json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class change_format:
	def __init__(self, filename):
		self.filename = filename
		self.dictionarify_the_Qs()

	
	def dictionarify_the_Qs(self):
		
		self.questions = []
		with open ("../database/question_links/"+self.filename, "r") as f:
			self.questions = f.readlines()

		self.stop_words = set(stopwords.words('english'))


		self.filtered_questions={}

		#removing last extra '\n'
		for question in self.questions:
			filtered_question=[]
			question = question[22:-1]
			question_backup=question

			#replacing '-' with ' '
			characters = list(question)
			question=""
			for character in characters:
				if character == '-':
					question+=' '
				else:
					question+=character
			
			#tokenize into words
			words = word_tokenize(question)
			#removing common words
			filtered_queston = [word for word in words if not word in self.stop_words]
			
			"""
			rest of the magic here using user-defined and built-in functions

			"""

			self.filtered_questions[question_backup] = filtered_queston

		with io.open("../database/formatted_questions/"+self.filename, 'w', encoding='utf8') as json_file:
			json.dump(self.filtered_questions, json_file, ensure_ascii=False)

if __name__ == '__main__'
	c = change_format("BITSAT-Preparation.txt")