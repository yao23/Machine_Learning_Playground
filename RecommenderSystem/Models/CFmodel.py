# Collaborative filtering model
import numpy as np
from sklearn.neighbors import NearestNeighbors
import logging


class CFmodel():
	RARECASE_THRESHOLD = 5
	logging.basicConfig(level=logging.INFO)

	def __init__(self):
		self.log = logging.getLogger(__name__)

	def _CFSVD(self, ratingsMat):


	def train(self, ratingsMat, itemFeatureTable):
		# itemFeatureTable is used for content-based model, which will predict for those items with few ratings
		# SVD will be used for collaborative filtering after the rare items have enough ratings

	def predict(self, userId):


	def provideRec(self, userId):
