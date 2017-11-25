# most popular model
# here it is a simple design: find the one with highest score with most of the users

class MostPopularModel():
	N_Freq_limit = 0.001

	def __init__(self):
		pass

	def train(self, history):
		# X must be a dataframe, with the second key as itemID, and third key as ratings

	def predict(self,X):
		# X can only be a list of itemID's

	def provideRec(self):
