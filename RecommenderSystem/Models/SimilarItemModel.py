# similar item model
# underneath it is to use a clustering model
# for simplicity, return all in the same cluster if rating is higher or equal to 3; return empty cluster otherwise

class SimilarItemModel():
	THRESHOLD = 3.0 # if ratings are below threshold, it will not be used

	def __init__(self,clusteringModel):

	def train(self, itemFeature, rating):
		# only single record
		# each model learns one person's current interest

	def predict(self, itemFeature):
		# X should be item's category feature, only single record
		# return the similar items

	def provideRec(self):

