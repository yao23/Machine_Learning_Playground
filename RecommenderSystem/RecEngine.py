# Recommendation Engine

from ModelStore import ModelStore
import logging

from DatabaseInterface import DatabaseInterface

class RecEngine(object):
	logging.basicConfig(level=logging.INFO)

	def __init__(self, userAnalyzer, modelStore, userActivityTable):
		self.userAnalyzer = userAnalyzer
		self.ModelStore = modelStore
		self.userActivityTable = userActivityTable

	def provideRecommendation(self, request):
		[userType, userId, request] = self.userAnalyzer.analyze(request, userActivityDB=DatabaseInterface.dbTable[
			'user_activity'])
		if userType == "anonymous":
			print "anonymous user: provide popular movies"
		elif userType == "new":
			print "new registered user: cold start"
		else:
			print "old user: recommend based on history"


