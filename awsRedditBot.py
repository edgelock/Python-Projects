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

subreddit = reddit.subreddit("redditdev")
print(subreddit.title)

#Prints the top 10 hot submissions in the learnpython subreddit along with their rank, score, URL and ID.
for submission in reddit.subreddit("AWSCertifications").hot(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.url)
    print(submission.id)
#Prints out comments in subreddit(s) of your choosing. 
for comment in reddit.subreddit("AWSCertifications").comments():
    print(comment.body)
    #Defining a "trigger phrase" to look for in the body of comments
    trigger_phrase = "SAP"
    #For all the comments in the subreddit(s) if the trigger phrase is met, print them out
    for comment in reddit.subreddit("AWSCertificatons").stream.comments():
        if trigger_phrase in comment.body.lower():
            print(comment.body)
 