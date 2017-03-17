#import xyz libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def format_(inp_string):
	
	stop_words = set(stopwords.words('english'))
	
	words = word_tokenize(inp_string)
			
	#removing common words(stopwords)
	filtered_string = [word for word in words if not word in stop_words]
	
	"""
	more magic on filtered_string in list format

	"""
	return filtered_string