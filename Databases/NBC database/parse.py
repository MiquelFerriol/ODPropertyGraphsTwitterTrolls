import pandas as pd
import ast

tweets = pd.read_csv("tweets_cut.csv",
                     sep=",")

hashtags = pd.DataFrame()

for id in range(0, tweets.shape[0]):
    row = tweets.loc[id]
    for elem in ast.literal_eval(row.hashtags):
        hashtags = hashtags.append({"hashtag": elem, "tweet_id": row.tweet_id}, ignore_index=True)


hashtags = hashtags.dropna(axis=0, how="any")  # remove rows with NA
hashtags = hashtags.drop_duplicates()  # remove repeated rows

hashtags.to_csv("hashtags.csv", sep=",", index=False)
