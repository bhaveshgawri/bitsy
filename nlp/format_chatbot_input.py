#import xyz libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def format_(inp_string):
	
	stop_words = set(stopwords.words('english'))
	
	words = word_tokenize(inp_string)
			
	#removing common words(stopwords)
	filtered_string = [word for word in words if not word in stop_words]
	"""
	#one liner mensioned above
	filtered_string=[]
	for w in words:
	if w not in stop_words:
		filtered_string.append(w)
	"""
	
	"""
	more magic on filtered_string in list format

	"""
	return filtered_string
