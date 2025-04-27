import requests
import praw
import tweepy
import yaml
from bs4 import BeautifulSoup

def load_config(filename="config.yml"):
    with open(filename, "r") as file:
        return yaml.safe_load(file)

config = load_config()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=config["reddit"]["client_id"],
    client_secret=config["reddit"]["client_secret"],
    user_agent=config["reddit"]["user_agent"]
)

# Initialize Twitter API
auth = tweepy.OAuthHandler(config["twitter"]["api_key"], config["twitter"]["api_secret"])
auth.set_access_token(config["twitter"]["access_token"], config["twitter"]["access_secret"])
twitter_api = tweepy.API(auth)

def fetch_reddit_trends(subreddit="giftsuggestions", limit=5):
    """Fetch top trending gift ideas from Reddit."""
    posts = reddit.subreddit(subreddit).hot(limit=limit)
    return [post.title for post in posts]

def fetch_twitter_trends(keyword="gift", count=5):
    """Fetch trending tweets related to gift ideas."""
    tweets = tweepy.Cursor(twitter_api.search_tweets, q=keyword, lang="en").items(count)
    return [tweet.text for tweet in tweets]

def fetch_local_store_gifts(query="unique gifts", location="New York"):
    """Scrape local store listings for unique gifts."""
    search_url = f"https://www.google.com/search?q={query}+in+{location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = []
    for a_tag in soup.find_all("a", href=True):
        if "maps" not in a_tag["href"] and "google" not in a_tag["href"]:
            links.append(a_tag["href"])
    return links[:5]  # Return top 5 local store links