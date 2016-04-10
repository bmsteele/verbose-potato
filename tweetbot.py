from twython import Twython, TwythonError
import time
# Api info goes here
APP_KEY = 'XXXX'
APP_SECRET = 'XXXX'
OAUTH_TOKEN = 'XXXX'
OAUTH_TOKEN_SECRET = 'XXXX'
#Use Twython to set up api access to twitter
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Read the things we need to tweet
with open('tweets.txt', 'r+') as tweetsfile:
	# Add each line from file to a list
	tweets = tweetsfile.readlines()
	# Loop through all the tweets
	for line in tweets[:]:
		try:
			# Skip empty list items
			if not line.strip():
				continue
			else:
				# What are we tweeting
				print ("Trying to tweet: " + line)
				# Attempt to send the tweet
				api.update_status(status=line)
				# Rate limit
				time.sleep(5)
		except TwythonError as e:
			# Oh crap, something went wrong
			print e
	# Yey it worked
	print ("I have tweeted AllTheThings!")
