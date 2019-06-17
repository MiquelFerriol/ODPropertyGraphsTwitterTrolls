# ODPropertyGraphsTwitterTrolls
Social networks play a very important role nowadays. They provide a way of communicating with all kinds of people and it is a source of news (though many times not too reliable). During the US 2016 presidential elections, social networks were used to influence the constituents’ votes. The Mueller report proved the suspicions that a state-sponsored actor tried to influence the elections, and that social platforms such as “YouTube, Facebook, Instagram, and Twitter” were used for that purpose.
The purpose of this project will be to analyze Twitter to study how Russian trolls influenced the elections and the extent of their influence.

## File info
- parse.py: It parses the CSV into a compatible format for being used by load.py
- load.py: It loads the NBC files into Neo4j database
- internetArchiveScraping.py: Reads the exhibit_b.csv and retrieves the available info about the users and creates the file avail_url.txt.
- twitterIAScrapper.py: Reads the avail_url.txt and for each URL retrieves all the information and stores the results in tweets_full.json
- scrappedLoad.py: Loads the tweets_full.json and imports it into Neo4j
- requierements.txt: Contains the libraries needed for python to execute the different .py files
