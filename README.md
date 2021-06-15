# City-Sentiment-Detector-BERT
Classifying tweets from cities into Positive and Negative sentiment and determining happiness of that city.

# Project Description:
The aim of this project is to perform sentiment analysis of tweets collected from selected cities and get an overall sentiment of that city.
Project consists of:-
- Pretrained BERT base model fine tuned on 'Sentiment140 Dataset' by Stanford University which is 1.6 million row dataset consisting of tweets.
The fine tuned model gave an accuracy of 86+ % compared to algorithms like Logistic Regression, Naive Bayes, etc which gave an accuracy of 77% only.

The model was retrained on single epoch consisting on ~65k steps over a period of 7 days.

# Running project locally:
- Install all libraries :- transformers, google_trans_new, tweepy, pandas, numpy, tensorflow, nltk, bs4 and re
- Create twitter developer account and get api credentials and input them in 'TweetMining'.
- Run 'TweetMining' Notebook to get live tweets.
- Run 'BERT_Sentiment140' notebook to classify tweets and to get city happiness score.

# Data Preprocessing:
- Extracted only 'text' & 'target' columns
- Dropped null values
- Cleaned tweets by removing links, xml, converting text to lowecase and tokenising words
- Shuffled rows of dataframe to get balanced dataset (Can be improved more)
- Transformed label '4' to '1' in dataset so as to use SparseCategoricalCrossentropy loss
- Converted dataset to BERT example format
- Converted above format to tf format

# Training:
- Preprocessed data is passed to BERT model for finetuning. 'Adam' optimizer (learning_rate=3e-5,epsilon=1e-08,clipnorm = 1.0) is used along with 'SparseCategoricalCrossentropy' loss and 'SparseCategoricalAccuracy' accuracy.
- Model is retrained on 1 epoch with ~65k steps. Accuracy of over 86% was achieved after training for 7 days.

# Project Flow:
- Connection to twitter api is established using tweepy wrapper for python using credentials.
- 1000 Tweets are mined according from different cities by entering city lat, lon and radius.
- The tweets are cleaned and non english tweets are translated by using google translate api.
- The cleaned and translated tweets are stored as dataframe with columns 'text' and 'city'
- The dataframe is passed through the retrained model with a softmax layer added for classification.
- The postive and negative sentiments of each tweet per city are counted and a ratio is postive tweets to negative is taken to guage the sentiment of that particular city.

# Modules:
- 'BERT_Sentiment140' is the main notebook where finetuning and sentiment analysis is performed.
- 'TweetbyLoc' is a util module for establishing connection to twitter api and mining tweets by location using tweepy wrapper.
- 'TweetMining' is the notebook where 'TweetbyLoc' is called and where tweets are mined, translated and stored in a csv format.

# Further Improvements to be made:
- Making code more modular.
- User input for cities instead of predefined cities.
- Creating and deploying a dashboard for displaying tweets mined with a choropleth map visualising sentiments of the cities.

Note: All processed csv files are created and stored in 'data' directory.


