import requests

url = "https://api.github.com/repos/psf/requests/pulls?state=open"
response = requests.get(url)
prs = response.json()

for pr in prs:
    number = pr["number"]
    title = pr["title"]
    author = pr["user"]["login"]
    base = pr["base"]["ref"]
    print(f"#{number}  {author}  -> {base}  {title}")