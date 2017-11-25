# main.py
# simulate different request coming into the system

from Webserver import WebServer, Request, Action

configMap = {"numberToServe": 10, "data_dir": "DATA"}
server = WebServer(configMap)
server.start() # load all the data in the database, start the first model training

# now experiment
reqX1 = Request(userId='X1')
req1 = Request(userId=1) # if it is a registered user, we use integer
print(reqX1)
print(req1)

recX1 = server.renderRecommendation(reqX1)
print recX1
#
# rec1 = server.renderRecommendation(req1)
# print(rec1)

action1 = Action(1, 255, 5)
print server.getFromInventory(255)
server.getAction(action1)
rec1_afteraction = server.renderRecommendation(req1)
print(rec1_afteraction)

actionX1 = Action('X1', 123, 5)
print server.getFromInventory(255)
server.getAction(actionX1)
recX1_afteraction = server.renderRecommendation(reqX1)
print(recX1_afteraction)

server.increment()
recX1_aftercleaning = server.renderRecommendation(reqX1)
print(recX1_aftercleaning)


req19 = Request(userId=19) # the one with very few history
rec19 = server.renderRecommendation(req19)
print(rec19)