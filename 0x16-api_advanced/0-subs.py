#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Define the URL to query subreddit details
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set custom User-Agent to prevent Too Many Requests error
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Linux; Reddit API Query)"
    }
    try:
        # Send GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the status code is not 200, return 0
        if response.status_code != 200:
            return 0 
        # Parse the response JSON to get the "data" section
        results = response.json().get("data")
        # If "data" is missing or None, return 0
        if results is None:
            return 0 
        # Return the number of subscribers
        return results.get("subscribers", 0)
    except (requests.RequestException, ValueError):
        # If any exception occurs during request or JSON parsing, return 0
        return 0
