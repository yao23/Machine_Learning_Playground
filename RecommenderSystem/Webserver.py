# A simulation framework
import logging

from DatabaseInterface import DatabaseInterface
from RecEngine import RecEngine
from Ranker import Ranker
from Learners.OfflineLearner import OfflineLearner
from Learners.OnlineLearner import OnlineLearner
from UserAnalyzer import UserAnalyzer
from ModelStore import ModelStore


class WebServer(object):
	logging.basicConfig(level=logging.INFO)

	def __init__(self, configMap):
		self.db = DatabaseInterface(configMap['data_dir'])
		self.numberToServe = configMap['numberToServe']
		self.log = logging.getLogger(__name__)
		self.userAnalyzer = UserAnalyzer
		self.ModelStore = ModelStore
		self.Ranker = Ranker(numberToServe=self.numberToServe, database=self.db)
		self.RecEngine = RecEngine(self.userAnalyzer, self.ModelStore, DatabaseInterface.dbTable['user_activity'])
		self.OnlineLearner = OnlineLearner
		self.OfflineLearner = OfflineLearner

	# numberToServe: the number of items finally served to the users
	def start(self):
		# each object here simulates the API calls through network
		# passing an object A to the constructor of B means A will communication to B


	def getAction(self,action):
		self.db.putAction(action=action)
		self.OfflineLearner.pushModel(self.ModelStore.getModel(self.ModelStore, ModelStore.KNN_MODEL_KEY), action.userId)

	def provideRecommendation(self, request):
		# return the ID's for the recommended items
		recommendations = self.RecEngine.provideRecommendation(request)
		self.Ranker.rerank((request.userId, recommendations))

	def renderRecommendation(self, request):
		[userType, userId, request] = self.userAnalyzer.analyze(request, userActivityDB=DatabaseInterface.dbTable['user_activity'])
		if userType == "anonymous":
			print "anonymous user: provide popular movies"
		elif userType == "new":
			print "new registered user: cold start"
		else:
			print "old user: recommend based on history"
		self.provideRecommendation(request=request)

	def increment(self):
		self.log.info("incrementing the system, update the models")
		# increment the whole system by one day, trigger offline training
		self.OfflineLearner.trainModel()

	def getFromInventory(self, itemId):
		return self.db.extract(DatabaseInterface.INVENTORY_KEY).loc[itemId]

# simulate a web request
class Request(object):
	def __init__(self, userId):
		self.userId = userId

	def __str__(self):
		return "request for user: "+str(self.userId)

# simulate a tracking event or a user's rating
class Action(object):
	def __init__(self, userId, itemId,rating):
		self.userId = userId
		self.itemId = itemId
		self.rating = rating

	def __str__(self):
		return "user: %s, item: %s, rating %s" %(self.userId, self.itemId, self.rating)