# Offline Learner
# Read in user history data, make models

from ModelStore import ModelStore
from DatabaseInterface import DatabaseInterface
import logging
import numpy as np

class OfflineLearner(object):
	logging.basicConfig(level=logging.INFO)
	THRESHOLD_FOR_LR = 3.

	def __init__(self, database, modelStore):
		self.database = database
		self.modelStore = modelStore
		self.log = logging.getLogger(__name__)
		self.modelRegistry = [(ModelStore.KNN_MODEL_KEY, "k nearest neighbor most popular model"),
								(ModelStore.MP_MODEL_KEY, "most popular item model"),
								(ModelStore.CL_MODEL_KEY, "item feature clustering model"),
								(ModelStore.CF_MODEL_KEY, "collaborative filtering model")]

	def trainModel(self):


	def pushModel(self, model, key):
