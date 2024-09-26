#!/usr/bin/python3
"""This script will return the number of subscribers associated with
a subreddit
"""
import json
"""
Script to print hot posts on a given Reddit subreddit.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """Method get the number of users subscribed to a subreddit
    subreddit (Str)- subreddit to check
    Returns - number of users (INT) else 0 (INT) if not subreddit is found
    """
    try:
        h = {'user-agent': 'Mozilla/5.0', 'allow_redirects': 'false'}
        p = {'limit': 10}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(url, headers=h, params=p).json().get('data')
        for post in req.get('children'):
            print(post.get('data', None).get('title', None))
    except Exception as e:
        print(None)
if __name__ == "__main__":
    pass

 """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }
    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return
    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")
    # Print the titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
