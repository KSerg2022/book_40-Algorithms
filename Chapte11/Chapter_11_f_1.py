"""
Алгоритмы обработки данных
ПРАКТИЧЕСКИЙ ПРИМЕР — АНАЛИЗ ТОНАЛЬНОСТИ ТВИТОВ В РЕЖИМЕ РЕАЛЬНОГО ВРЕМЕНИ
"""

print('\n1 -- ')
# step 1
import tweepy, json, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# step 4
twitter_access_token = < your_twitter_access_token >
twitter_access_token_secret = < your_twitter_access_token_secret >
twitter_consumer_key = < your_consumer_key >
twitter_consumer_secret = < your_twitter_consumer_secret >

# twitter_access_token = "966112597975150592-I6l9SD8IOj3OYmQBkOnNeRLr3lyqsrN"
# twitter_access_token_secret = "HR3Eiyfh3kG16zTraLdXCtcNLMhXOdU23UH8cYfNkzRBV"
# twitter_consumer_key = "rjQVbO0NyrvcuJDT91752ex11"
# twitter_consumer_secret = "zufLHHrPOWN1sF8JocuB36wj4yZWscIwUGwQYkh8TYfCG9aRIG"

# step 5
auth = tweepy.OAuthHandler(twitter_consumer_key,
twitter_consumer_secret)
auth.set_access_token(twitter_access_token,
twitter_access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# step 6
news_sources = ("@BBC", "@ctvnews", "@CNN","@FoxNews", "@dawn_com")

# step 7
# We start extracting 100 tweets from each of the news sources
print("...STARTING..... collecting tweets from sources")

# Let us define an array to hold the sentiments
array_sentiments = []

for user in news_sources:
    count_tweet = 100  # Setting the twitter count at 100
    print("Start tweets from %s" % user)
    for x in range(5):  # Extracting 5 pages of tweets
        public_tweets = api.user_timeline(user, page=x)
        # For each tweet
        for tweet in public_tweets:
            # Calculating the compound,+ive,-ive and neutral value for each tweet
            compound = analyzer.polarity_scores(tweet["text"])["compound"]
            pos = analyzer.polarity_scores(tweet["text"])["pos"]
            neu = analyzer.polarity_scores(tweet["text"])["neu"]
            neg = analyzer.polarity_scores(tweet["text"])["neg"]

            array_sentiments.append({"Media": user,
                                     "Tweet Text": tweet["text"],
                                     "Compound": compound,
                                     "Positive": pos,
                                     "Negative": neg,
                                     "Neutral": neu,
                                     "Date": tweet["created_at"],
                                     "Tweets Ago": count_tweet})

            count_tweet -= 1

print("DONE with extracting tweets")


# Creating a dataframe from the Sentiment Array Converting the sentiment arrary to a dataframe
sentiments_df=pd.DataFrame.from_dict(array_sentiments)
# Removing the '@' from Media column in the data frame
sentiments_df['Media'] = sentiments_df['Media'].map(lambda x: x.lstrip('@'))

# Re_arranging the order of columns before saving into CSV file
sentiments_df=sentiments_df[["Media","Date","Tweet Text","Compound","Positive","Negative","Neutral","Tweets Ago"]]
# Storing into a CSV File\
sentiments_df.to_csv("mySentimentAnalysis.csv")

sentiments_df.head(10)

# Creating an array with the unique Media sources in the data frame
source=sentiments_df["Media"].unique()


# step 8
for media in source:
    mydf=sentiments_df[sentiments_df["Media"]==media]
    plt.scatter(mydf["Tweets Ago"],mydf["Compound"], marker="o", linewidth=0, alpha=0.8, label=media,
                facecolors=mydf.Media.map({"BBC": "pink", "ctvnews" : "purple",  "CNN": 'red',
                                              "FoxNews":"blue","dawn_com":"green"}))

plt.legend(bbox_to_anchor = (1,1),title="Media Sources")
plt.title("Sentiment Analysis of Media Tweets (%s)" % (time.strftime("%x")), fontsize=14)
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")
plt.xlim(101,0)
plt.ylim(-1,1)
plt.grid(True)
plt.savefig("Output/Sentiment Analysis of Media Tweets.png",bbox_inches='tight')
plt.show()


# step 9
# Calculating the mean for each Media channel and storing to a dataframe
means_media_trends=sentiments_df.groupby("Media").mean()["Compound"].to_frame()
#Resetting the index
means_media_trends.reset_index(inplace=True)

print(means_media_trends)


