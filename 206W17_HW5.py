import unittest
import tweepy
import requests
import json
import twitter_info

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time: Friday, 9am - 10am
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice 
#(should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) 
#of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
# https://apps.twitter.com/app/13422883/keys

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.

CACHE_FNAME = "HW5_cache.json" # text represents data you got when you made request; you can store dictionary as string formatted in JSON way
try: 
	cache_file_obj = open(CACHE_FNAME, 'r')
	cache_contenst = cache_file_obj.read() # pull all into one big string
	CACHE_DICTION = json.loads(cache_contents) # dictionary that holds all cache data  
except:
	CACHE_DICTION = {}

def get_tweets(value):
	unique_identifier = "twitter_{}".format(value)
	if unique_identifier in CACHE_DICTION:
		print("using cached data for ", value)
		twitter_results = CACHED_DICTION[unique_identifier] #get that data!
	else:
		print("getting data from internet for", value)
		twitter_results = api.search(q = value)
		CACHE_DICTION[unique_identifier] = twitter_results #add it to the dictionary
		f = open(CACHE_FNAME, "w")
		f.write(json.dumps(CACHE_DICTION)) #make the whole dictionary holding data
		f.close()
	#no matter what you have, run the for loop to get everything!
	text_list = []
	for i in range(len(twitter_results)):
		tweet_text = twitter_results["statuses"][i]["text"]
		tweet_time = twitter_results["statuses"][i]["created_at"]
		temp_tup = (tweet_text, tweet_time)
		text_list.append(temp_tup)
	print(text_list)
	print("That was text_list")
	for i in range(len(text_list)):
		print("TEXT: ", text_list[i][0])
		print("CREATED AT: ", text_list[i][1])
		print("\n")

	return(text_list)

print(get_tweets("adele"))

# 	text_dict = {}
# 	for i in range(len(twitter_results)):
# 		tweet_text = twitter_results["text"][i]
# 		tweet_time = twitter_result["created at"][i]
# 		text_dict[tweet_text] = tweet_time
# 	return(text_dict)

# print(get_tweets("university of michigan"))









# CACHE_FNAME = "HW5_cache.json"
# try:
# 	cache_file_obj = open(CACHE_FNAME,'r')
# 	cache_contents = cache_file_obj.read()
# 	CACHE_DICTION = json.loads(cache_contents) #all the data you cache available
# except:
# 	CACHE_DICTION = {} 

# def canonical_order(d):
#     alphabetized_keys = sorted(d.keys())
#     res = []
#     for k in alphabetized_keys:
#         res.append((k, d[k]))
#     return res
    
# def requestURL(baseurl, params = {}):
#     req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
#     prepped = req.prepare()
#     return prepped.url

# def twitter_caching(value):
# 	baseurl = 
# 	results = api.search(q = value)
# 	print(results)





























# CACHE_FNAME = "cache_file.json" # text represents data you got when you made request; you can store dictionary as string formatted in JSON way
# try: 
# 	cache_file_obj = open(CACHE_FNAME, 'r')
# 	cache_contenst = cache_file_obj.read() # pull all into one big string
# 	CACHE_DICTION = json.loads(cache_contents) # dictionary that holds all cache data  
# except:
# 	CACHE_DICTION = {}
# 	# I know in my code, inside a function that gets data from the internet, I will have to make sure
# 	# that I properly add data to CACHE_DICTION
# 	# I will have to make sure that I properly write CACHE_DICTION to a file so that I have it next time I run my program
# 	# what are the parameters, have I gotten this data before, etc.







