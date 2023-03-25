import requests
import json
import random
import html
import time

# set URL and perhaps useless dictionary to reference/use
url = "https://opentdb.com/api.php/"
query_dict = {
    "amount" : range(1, 101), 
    "category" : list(range(9, 32)), 
    "difficulty" : ["easy", "medium", "hard"], 
    "type" : [True, False]
    }  

# pick some random categories
cat_numbs = [0,1,2]
for q in range(3) : cat_numbs[q] = random.randint(9, max(query_dict["category"]))

# get the names of the random categories from the trivia API
cat_names = [0, 1, 2]
querystring = {
    "category" : cat_numbs,
    "amount" : 1
    }
for q in range(len(cat_names)):
    response = requests.get(url = url, 
                            params = {"amount" : querystring["amount"],
                                    "category" : querystring["category"][q]
                                    }
                            )
    results = json.loads(response.text)
    cat_names[q] = results["results"][0]["category"]

# discard any duplicated names
final_cats = []
[final_cats.append(category) for category in cat_names if category not in final_cats]

# start game, user choose category and question count
print("Welcome to TriviaBot 5ThouThou, Please select a category of Trivia:\n")
for x in range(len(final_cats)):
    print(str(x + 1) + " - " + str(final_cats[x]))
cat = int(input())
print("You picked " + str(final_cats[cat - 1])  +  ", how many questions would you like?")
q_count = int(input())

# acquire questions from the trivia API with a random difficulty level
cat_dict = {}
for x in range(len(final_cats)) : cat_dict[x + 1] = [cat_numbs[x], final_cats[x]]
querystring = {
    "amount" : q_count,
    "category" : cat_dict[cat][0],
    "difficulty" : query_dict["difficulty"][random.randint(0, 2)]
    }
response = requests.get(url, params = querystring)
results = json.loads(response.text)

# load each question
q = {}
for x in range(len(results["results"])) : q[x] = results["results"][x]

# set count for correct answers and start the game
correct = 0
for x in range(len(q)):
    count = 1
    answers = dict()
    s_answers = dict()
    answer_key = list()
    answers[q[x]["correct_answer"]] = 1
    for ans in q[x]["incorrect_answers"] : answers[ans] = 0
    keys = list(answers.keys())
    random.shuffle(keys)
    for key in keys : s_answers.update({key : answers[key]})
    print("Question " + str(x + 1) +  "\n" + str(html.unescape(q[x]["question"])))
    for choice in s_answers:
        print(str(count) + " : " + str(html.unescape(choice)))
        answer_key.append(choice)
        count += 1
    answer = int(input())
    if answer_key[answer - 1] == q[x]["correct_answer"]: 
        print("Correct!")
        correct += 1
    else:
        print("Sorry, that was incorrect.")

# thanks for reading!
print("Thanks for playing the game!\nYou got " + str(correct)  + " out of " + str(q_count)  + " correct.")