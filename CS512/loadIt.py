#%%
from array import array
import pandas as pd


#//TODO this loadIt.py should be extended to take a path to a json file and return a csv will need to continue this on to determine if the json file is lines = True or in normal json

# load business data to the workspace
business_json_path = 'D:\zz\OneDrive\Documents\File Cabinet\Get Smart\MS\zzData\yelp\yelp_academic_dataset_business.json'
# use pandas string data type to access the methods
bus_df = pd.read_json(
    business_json_path,
    dtype = {
        'business_id': pd.StringDtype(), # unique id
        'name': pd.StringDtype(), # busines name
        'address': pd.StringDtype(), # street address
        'city': pd.StringDtype(),
        'state': pd.StringDtype(),
        'postal code': pd.StringDtype(),
        'latitude': float,
        'longitude': float,
        'stars': float, # rounded to half-stars
        'review_count': int,
        'is_open': int, # 1 for open 0 for closed
        'attributes': object, # some attribute values might be objects
        'categories': pd.StringDtype(), # strings of business categories
        'hours': object # key day to value hours. hours use 24h
        },
    lines = True
    )
# drop business that are closed 1 == open...0 == closed
bus_df = bus_df[bus_df['is_open'] == 1]
# drop columns that are irrelevant
bus_df.drop(
    columns = [
        'address', # to map the business only need lat/long
        'city',
        'state',
        'postal_code',
        'is_open', # all -> closed were dropped
        'hours', # not needed
        'attributes' # not needed
        ],
    inplace = True # don't create a new DataFrame modify the original
    )
#BOOKMARK formatting business
# "this is, a, string" -> ["this is", "a", "string"]
bus_df['categories'] = bus_df['categories'].str.split(",")
# explode the column: 1 row per 'category' for each and reindex 
bus_df_exploded = bus_df.explode('categories', ignore_index = True) 
bus_df_exploded['categories'] = bus_df_exploded['categories'].str.strip()
bus_df_exploded['categories'] = bus_df_exploded['categories'].str.lower() # lower case everything
unique_categories = bus_df_exploded['categories'].unique() # unique values
count_categories = bus_df_exploded['categories'].value_counts() # count of each unique value
#NOTE line 53/54 necessary to not get duplicate "restaurants" "restaurants "....
clean_business_df = bus_df_exploded[bus_df_exploded['categories'].str.contains(
                                                                            'restaurants',
                                                                            case = False,
                                                                            na = False
                                                                            )]
clean_business_df.reset_index(drop = True) # reset index explode carries duplicates
# load review data to the workspace
review_json_path = 'D:\zz\OneDrive\Documents\File Cabinet\Get Smart\MS\zzData\yelp\yelp_academic_dataset_review.json'
#NOTE use pd.StringDtype() to activate the pandas .str functionality if needed
review = pd.read_json(
    review_json_path,
    dtype = {
        'review_id': pd.StringDtype(), # unique
        'user_id': pd.StringDtype(), # unique - maps to user ID in users.json
        'business_id': pd.StringDtype(), # maps to business in business.json
        'stars': int, # rating
        'date': pd.StringDtype(), # string yyyy-mm-dd
        'text': pd.StringDtype(), # the review
        'useful': int, # useful votes received
        'funny': int, # funny votes received
        'cool': int # cool votes received
        },
    chunksize = 1000000, # 
    lines = True
    )
#NOTE utilize the chunk object created above.  drop irrelevant columns, rename column as both data sets contain 'stars'.  Merge inner and stack the chunks in a list to be put back together
chunks = []
for rev_chunks in review:
    rev_chunks = rev_chunks.drop(['review_id', 'user_id', 'useful', 'funny', 'cool'], axis = 1)
    rev_chunks = rev_chunks.rename(columns = {'stars': 'review_stars'})
    chunk_merge = pd.merge(clean_business_df, rev_chunks, on = 'business_id', how = 'inner')
    chunks.append(chunk_merge)
rev_bus = pd.concat(chunks, ignore_index = True, join = 'outer', axis = 0) 
rev_bus['text'] = rev_bus['text'].str.strip(',')
rev_bus['text'] = rev_bus['text'].str.lower()

#BOOKMARK write merged data to csv and json
#TODO possibly write these to more smaller files?
rev_bus.to_csv('D:/zz/OneDrive/Documents/File Cabinet/Get Smart/MS/zzData/yelp/business_review.csv')
rev_bus.to_json(
    path_or_buf = 'D:/zz/OneDrive/Documents/File Cabinet/Get Smart/MS/zzData/yelp/business_review.json',
    orient = "index"
    )


#%%
#NOTE Code below untouched.
#TODO move all of the keys from bus_df['attributes'] to Column headers & apply boolean. 
# 1 if they have true value for the key column, 0 if they don't have the key or have false
# only unique values into the column headers.  If we want to use the attributes.

for row in bus_df['attributes']:
    try:
        for key in row:
            if key not in bus_df.columns:
                bus_df[key] = None
            else:
                pass
    except TypeError:
        pass

#%% 
# load checkin data to the workspace
checkin_json_path = 'D:\zz\OneDrive\Documents\File Cabinet\Get Smart\MS\zzData\yelp\yelp_academic_dataset_checkin.json'

checkin = pd.read_json(
    checkin_json_path,
    lines = True
    )

#%%
# load tip data to the workspace
# tips are written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.
tip_json_path = 'D:\zz\OneDrive\Documents\File Cabinet\Get Smart\MS\zzData\yelp\yelp_academic_dataset_tip.json'

tip = pd.read_json(
    tip_json_path,
    lines = True
    )

#%%
# load user data into the workspace
user_json_path = 'D:\zz\OneDrive\Documents\File Cabinet\Get Smart\MS\zzData\yelp\yelp_academic_dataset_user.json'

user = pd.read_json(
    user_json_path,
    lines = True
    )
