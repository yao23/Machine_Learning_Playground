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

	# numberToServe: the number of items finally served to the users
	def start(self):
		# each object here simulates the API calls through network
		# passing an object A to the constructor of B means A will communication to B


	def getAction(self,action):

	def provideRecommendation(self, request):
		# return the ID's for the recommended items

	def renderRecommendation(self, request):


	def increment(self):
		self.log.info("incrementing the system, update the models")
		# increment the whole system by one day, trigger offline training

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