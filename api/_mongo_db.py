import pymongo
from bson.objectid import ObjectId
from bson.son import SON
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, JSONOptions, CANONICAL_JSON_OPTIONS
from datetime import datetime

# mgUrl = "mongodb+srv://atlasadmin:123@instatecluster0-rugg4.gcp.mongodb.net/?retryWrites=true&SSL=true&ssl_cert_reqs=CERT_NONE"


class mongoDb:

 def __init__(self, url, name):
  self.client = pymongo.MongoClient(url)
  self.db = self.client[name]

 def addCollection(self, collection, data):
  self.db[collection].insert(data)

 def addDocumentToCollection(self, collection, data):
  col = self.db[collection]
  return col.insert_one(data).inserted_id

 def queryCollectionCols(self, collection):
  return list(self.db[collection].find({}, {'_id': 0, 'account': 0}))

 def queryCollection(self, collection, query):
  return list(self.db[collection].find(query))

 def queryCollectionById(self, collection, id):
  return self.db[collection].find_one({"_id": ObjectId(id)})

 def queryCollectionItem(self, collection, query):
  return self.db[collection].find_one(query)

 def updateItem(self, collection, qry, data):
  return self.db[collection].update_one(qry, data)

 def updateMany(self, collection, qry, data):
  return self.db[collection].update_many(qry, data)

 def updateItemByid(self, collection, id, data):
  return self.db[collection].update_one({"_id": ObjectId(id)}, data)

 def replaceItem(self, collection, id, data):
  return self.db[collection].replace_one({"_id": ObjectId(id)}, data)

 def getDistinctCollection(self, collection, qry, item):
  return self.db[collection].find(qry).distinct(item)

 def deleteItems(self, collection, qry):
  self.db[collection].delete_many(qry)

 def deleteItem(self, collection, qry):
  self.db[collection].delete_one(qry)

 def dropCollection(self, collection):
  self.db[collection].drop()
  return []

 def getDateRange(self, collection, start, end):
  return self.db[collection].find({"date": {"$gte": start, "$lte": end}})
