# Recommendation Engine

from ModelStore import ModelStore
import logging

from DatabaseInterface import DatabaseInterface
from Models.SimilarItemModel import SimilarItemModel
from Models.CFmodel import CFmodel
from Models.MostPopularModel import MostPopularModel

class RecEngine(object):
	logging.basicConfig(level=logging.INFO)

	def __init__(self, userAnalyzer, modelStore, userActivityTable):
		self.userAnalyzer = userAnalyzer
		self.ModelStore = modelStore
		self.userActivityTable = userActivityTable

	def provideRecommendation(self, request):
		recommendations = []
		[userType, userId, request] = self.userAnalyzer.analyze(request, userActivityDB=DatabaseInterface.dbTable[
			'user_activity'])
		if userType == "anonymous":
			print "anonymous user: provide popular movies"
			recommendations.append(MostPopularModel(self.modelStore.getModel(ModelStore.MP_MODEL_KEY)).provideRec())
		elif userType == "new":
			print "new registered user: cold start"
			recommendations.append(MostPopularModel(self.modelStore.getModel(ModelStore.MP_MODEL_KEY)).provideRec())
			recommendations.append(SimilarItemModel(self.modelStore.getModel(ModelStore.SI_MODEL_KEY)).provideRec())
		else:
			print "old user: recommend based on history"
			recommendations = []
			recommendations.append(MostPopularModel(self.modelStore.getModel(ModelStore.MP_MODEL_KEY)).provideRec())
			recommendations.append(SimilarItemModel(self.modelStore.getModel(ModelStore.SI_MODEL_KEY)).provideRec())
			recommendations.append(CFmodel(self.modelStore.getModel(ModelStore.CF_MODEL_KEY)).provideRec(request.userId))
		return recommendations


