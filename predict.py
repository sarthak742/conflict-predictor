from dotenv import load_dotenv
import os
import sys
load_dotenv()                         # 1. read .env, load its NAME=value lines
token = os.getenv("GITHUB_TOKEN") 
import requests

all_prs = []
page = 1
headers = {"Authorization": f"Bearer {token}"}
repo = sys.argv[1]
while True:
    url = f"https://api.github.com/repos/{repo}/pulls?state=open&per_page=100&page={page}"
    response = requests.get(url, headers=headers)
    prs = response.json()          # this one page's PRs
    if prs == []:                  # did this page come back empty?
        break
    all_prs.extend(prs)               # add this page's PRs to the big list
    page = page + 1

print(len(all_prs))
                                # load the library
for pr in all_prs:                                    # step 4: one PR at a time
    number = pr["number"]
    title = pr["title"]
    author = pr["user"]["login"]                  # dict inside a dict
    base = pr["base"]["ref"]
    print(f"#{number}  {author}  -> {base}  {title}")   # step 5