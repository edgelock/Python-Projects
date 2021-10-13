#You will have to run a !pip isntall praw to use this script.
import praw
import time #Imports the time inport so you can space out your iteraction with reddit
from prawcore.exceptions import ResponseException

#Reddit bot is connected & connected to said account.
reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
    username="my username",
    password="my password",
)
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#Check to see if you are properly authenticated
try:
    print("Authenticated as {}".format(reddit.user.me()))
except ResponseException:
    print("Something went wrong during authentication")

#Defining a "trigger phrase" to look for in the stream of submission titles (or wherever you may want to look)
trigger_phrase = "SAP-C01"
trigger_phrase2 = "GCP PCA"
#TODO Add a phrase for KCA
#trigger_phrase3 = ""

#For all the submission in the subreddit(s) if the trigger phrase is in said submission.title, print it out.
print("AWSCertifications Top 10:")
for count, submission in enumerate(reddit.subreddit("AWSCertifications").hot(limit=10)):
    print(count, submission.title)
print("\n")
print("Googlecloud Top 10:")
for count, submission in enumerate(reddit.subreddit("Googlecloud").hot(limit=10)):
    print(count, submission.title)
print("\n")
print("Azure Top 10:\n")
for count, submission in enumerate(reddit.subreddit("Azure").hot(limit=10)):
    print(count, submission.title)


 