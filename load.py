from py2neo import Graph
graph = Graph(password="admin")


def loadTweetsNBC(graph):
	query = """
LOAD CSV WITH HEADERS FROM "file:///tweets_cut.csv" AS csvLine FIELDTERMINATOR ',' 
WITH csvLine
WHERE csvLine.tweet_id IS NOT NULL
MATCH (t:Troll {id: csvLine.user_id})
MERGE (tw:Tweet {id: csvLine.tweet_id})
MERGE (u)-[:POSTED]->(tw)
ON CREATE SET tw.created_at = csvLine.created_at, tw.retweet_count = csvLine.retweet_count,
 tw.text = csvLine.text, tw.retweeted = csvLine.retweeted, tw.favourite_count = csvLine.favourite_count;
"""
	graph.run(query)


def loadHashtags(graph):
	query = """
LOAD CSV WITH HEADERS FROM "file:///hashtags.csv" AS csvLine FIELDTERMINATOR ','
WITH csvLine
MATCH (tw:Tweet {id: csvLine.tweet_id})
WHERE csvLine.hashtag IS NOT NULL
MERGE (h:Hashtag {hashtag: csvLine.hashtag})
MERGE (tw)-[:HAS_TAG]->(h)
"""
	graph.run(query)


def loadUsers(graph):
	query = """
LOAD CSV WITH HEADERS FROM "file:///users.csv" AS csvLine FIELDTERMINATOR ',' 
WITH csvLine
MERGE (t:Troll {id: csvLine.id})
ON CREATE SET t.location = csvLine.location, t.name = csvLine.name, t.followers_count = csvLine.followers_count,
t.statuses_count = csvLine.statuses_count, t.time_zone = csvLine.time_zone, t.verified = csvLine.verified, 
t.lang = csvLine.lang, t.screen_name = csvLine.screen_name, t.description = csvLine.description, t.created_at = csvLine.created_at,
t.favourites_count = csvLine.favourites_count, t.listed_count = csvLine.listed_count;
"""
	graph.run(query)


loadUsers(graph)
loadTweetsNBC(graph)
loadHashtags(graph)
