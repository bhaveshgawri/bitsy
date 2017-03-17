#import xyz library
import io, json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class formatted_dictionarify:
	def __init__(self, filename):
		self.filename = filename
		self.stop_words = set(stopwords.words('english'))
		self.filtered_questions={}
		self.dictionarify_the_Qs()
	
	def dictionarify_the_Qs(self):
		with open ("../database/question_links/"+self.filename, "r") as f:
			questions = f.readlines()

		self.formatify(questions)
		
		#JSONify
		with io.open("../database/formatted_questions/"+self.filename, 'w', encoding='utf8') as json_file:
			json.dump(self.filtered_questions, json_file, ensure_ascii=False)

	def formatify(self, questions):
		for question in questions:
			filtered_question=[]
			
			#'22' to remove 'http' part and '-1' to remove last '\n'
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
			
			#removing common words(stopwords)
			filtered_queston = [word for word in words if not word in self.stop_words]
			
			"""
			rest of the magic here using user-defined and built-in functions
			apply magic on filtered_question in list format

			"""
			self.filtered_questions[question_backup] = filtered_queston		


if __name__ == '__main__':
	fd = formatted_dictionarify("BITSAT-Preparation.txt")