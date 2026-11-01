import requests

all_prs = []
page = 1
while True:
    url = f"https://api.github.com/repos/psf/requests/pulls?state=open&per_page=100&page={page}"
    response = requests.get(url)
    prs = response.json()          # this one page's PRs
    if prs == []:                  # did this page come back empty?
        break
    all_prs.extend(prs)               # add this page's PRs to the big list
    page = page + 1

print(len(all_prs))
                                # load the library
for prs in all_prs:                                    # step 4: one PR at a time
    number = prs["number"]
    title = prs["title"]
    author = prs["user"]["login"]                  # dict inside a dict
    base = prs["base"]["ref"]
    print(f"#{number}  {author}  -> {base}  {title}")   # step 5