# Ranker

import logging
import numpy as np

# rank the items from each recommendation module
# highly influenced by business strategy and varies from system to system
from DatabaseInterface import DatabaseInterface


class Ranker(object):
	logging.basicConfig(level=logging.INFO)
	def __init__(self, numberToServe, database):

	def _getUsedItems(self, userId):

	def rerank(self,recommendationsTuple):
		# recommendationTupe is a tuple of (userId, recommendations)
		# recommendations is a dictionary of lists {RecType: Items}, RecType can be "online", "offline", "popular"
		# return the ranked recommendation
		# here is the strategy:
		# if the userId is -1, it means it is from anonymous user.
		# else remove the watched item and


