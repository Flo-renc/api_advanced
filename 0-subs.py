#!/usr/bin/python3
"""
function that queries Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries number of subscribers"""
   
   url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0
