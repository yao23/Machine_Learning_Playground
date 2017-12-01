# Online Learner
# take in the user action, serve models

from ModelStore import ModelStore
from DatabaseInterface import DatabaseInterface
import logging

class OnlineLearner(object):
	logging.basicConfig(level=logging.INFO)

	def __init__(self, database, modelStore):
		self.ModelStore = modelStore
		self.db = database

	def trainModel(self, action):

	def pushModel(self, model, userId):
		self.modelStore.setModel(model, key=self.ModelStore.CL_MODEL_KEY, memberId=userId)
