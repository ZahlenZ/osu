#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import string

from wordcloud import WordCloud
from collections import Counter

data_path = 'D:/zz/OneDrive/Documents/File Cabinet/Get Smart/MS/zzData/yelp/rev_bus.csv'
br_df = pd.read_csv(data_path)

too_common = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us", "was", "is", "hi", "are", "were", "t", "it", "i", "food", "great", "had", "place", "very", "here", "best", "restaurant", "ive", "been", "really", "got", "too", "has", "im", "ever", "more", "made", "try", "ordered", "order", "wait", "dont", "came", "eat", "meal", "always", "little", "lunch", "dinner", "breakfast", "went", "cant", "every", "everything","1", "2", "3", "4", "5", "off", "took", "again", "before", "did", "didnt", "said"]

#%% 1 star review work
# filter for only 1 star reviews
rev1star = br_df[br_df['review_stars'] == 1]
# hold onto only the reviews and reset the index
star1_reviews = rev1star['text']
star1_reviews = pd.DataFrame(star1_reviews).reset_index(drop = True)
# replace all of the pesky punctuation
star1_reviews['text'] = star1_reviews['text'].str.replace("[)!,.'(]",'')
# apply .join to each review to remove words that we aren't interest in
star1_reviews['text'] = star1_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in too_common]))
# create a long string of all of the words
star1_string = ' '.join(star1_reviews['text'])
# pull out each word from the string and add them to a list
star1_words = re.findall(r'\b\w+\b', star1_string)
# Counter function to count each element of the list 
star1_word_count = Counter(star1_words)
# Add the items from the list
star1_word_list = list(star1_word_count.items())
# Sort the list of words and there occurances decending (most to least)
star1_word_list = sorted(star1_word_list, key = lambda x: x[1], reverse = True)
# Create a dictionary of the top 25 words that remain so that they can be made into a word cloud
top25_1star = star1_word_list[0:25]
top25_1star = dict(top25_1star)
#%% 3 star review work

rev3star = br_df[br_df['review_stars'] == 3]
star3_reviews = rev3star['text']
star3_reviews = pd.DataFrame(star3_reviews).reset_index(drop = True)
star3_reviews['text'] = star3_reviews['text'].str.replace("[)!,.'(]",'')
star3_reviews['text'] = star3_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in too_common]))
star3_string = ' '.join(star3_reviews['text'])
star3_words = re.findall(r'\b\w+\b', star3_string)
star3_word_count = Counter(star3_words)
star3_word_list = list(star3_word_count.items())
star3_word_list = sorted(star3_word_list, key = lambda x: x[1], reverse = True)
top25_3star = star3_word_list[0:25]
top25_3star = dict(top25_3star)

#%% 5 star review work
rev5star = br_df[br_df['review_stars'] == 5]
star5_reviews = rev5star['text']
star5_reviews = pd.DataFrame(star5_reviews).reset_index(drop = True)
star5_reviews['text'] = star5_reviews['text'].str.replace("[)!,.'(]",'')
star5_reviews['text'] = star5_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() 
    if word.lower() not in too_common]))
star5_string = ' '.join(star5_reviews['text'])
star5_words = re.findall(r'\b\w+\b', star5_string)
star5_word_count = Counter(star5_words)
star5_word_list = list(star5_word_count.items())
star5_word_list = sorted(star5_word_list, key = lambda x: x[1], reverse = True)
top25_5star = star5_word_list[0:25]
top25_5star = dict(top25_5star)

#%%
# let the word clou package do the heavy lifting, feed it the dictionary
wordcloud = WordCloud(
    width = 800, height = 800, 
    background_color = 'white', 
    max_words = 50).generate_from_frequencies(top25_3star)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)

#%%
# plot the bar chart
words = list(top25_3star.keys())
counts = list(top25_3star.values())
plt.bar(words, counts)
plt.title('Word Frequency')
plt.xticks(rotation = 90)
plt.xlabel('Words')
plt.ylabel('Counts')