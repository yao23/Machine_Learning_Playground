# User Type Analyzer
# Determine different type of user, send different user to different recommendation module

class UserAnalyzer(object):
	def __init__(self):
		pass

	def analyze(self, request, userActivityDB):
		# should return an identifier such that the recommender engine knows what to do
		if isinstance(request.userId,str):
			# it is an anonymous request
			return ["anonymous", -1,  request]
		elif request.userId in userActivityDB.index:
			if userActivityDB[request.userId] >= 30:
				return ["old", request.userId, request]
			else:
				return ["new", request.userId, request]
		else:
			return ["new", request.userId, request]
			# raise Exception("User Id not registered")

	def analyzeAction(self, action):
		if isinstance(action.userId,str):
			return "anonymous"
		else:
			return "registered"
