#from langchain.tools import tool
from langchain_core.tools import tool
import requests
import re


@tool
def github_lookup(username: str):
    """
    Lookup GitHub profile.
    """

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)
    data = response.json()
    return f"GitHub profile for {username} is {data}"