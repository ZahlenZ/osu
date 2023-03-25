#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

data_path = 'D:/zz/OneDrive/Documents/File Cabinet/Get Smart/MS/zzData/yelp/rev_bus.csv'
br_df = pd.read_csv(data_path)

# create the dataframes for each star level
rev1star = br_df[br_df['review_stars'] == 1]
rev2star = br_df[br_df['review_stars'] == 2]
rev3star = br_df[br_df['review_stars'] == 4]
rev4star = br_df[br_df['review_stars'] == 4]
rev5star = br_df[br_df['review_stars'] == 5]

star1_reviews = rev1star['text']
star2_reviews = rev2star['text']
star3_reviews = rev3star['text']
star4_reviews = rev4star['text']
star5_reviews = rev5star['text']

star1_reviews = pd.DataFrame(star1_reviews).reset_index(drop = True)
star2_reviews = pd.DataFrame(star2_reviews).reset_index(drop = True)
star3_reviews = pd.DataFrame(star3_reviews).reset_index(drop = True)
star4_reviews = pd.DataFrame(star4_reviews).reset_index(drop = True)
star5_reviews = pd.DataFrame(star5_reviews).reset_index(drop = True)

too_common = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]

star1_reviews['text'] = star1_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in too_common]))

star3_reviews['text'] = star3_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in too_common]))

star5_reviews['text'] = star5_reviews['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in too_common]))

star1_string = ' '.join(star1_reviews[]
#%%
# stack the reviews with the star count we are interested in
poor_rev = pd.concat([rev1star, rev2star], axis = 0)
well_rev = pd.concat([rev4star, rev5star], axis = 0)
# extract just the column of text and create a long list of the words
good_words = well_rev['text']
big_string = ' '.join(good_words)

chunk_size = 10000
chunks = [big_string[i : i + chunk_size] for i in range(0, len(big_string), chunk_size)]

words = []
for chunk in chunks:
    matches = re.findall(r'\b\w+\b', chunk)
    words.extend(matches)

words = re.findall(r'\b\w+\b', string)
word_counts = Counter(good_words)
word_counts = list(word_counts.items()) 

good_words = []
for review in well_rev['text']:
    for word in re.findall(r'\b\w+\b', review):
        if word not in good_words:
            good_words.append(word)
        else:
            pass

poor_words = []
for review in poor_rev['text']:
    for word in re.findall(r'\b\w+\b', review):
        if word not in poor_words:
            poor_words.append(word)
        else:
            pass