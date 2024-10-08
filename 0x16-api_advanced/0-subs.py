#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Linux; Reddit API Query)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0 
        results = response.json().get("data")
        if results is None:
            return 0 
        return results.get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
