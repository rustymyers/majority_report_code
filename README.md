# majority_report_code
[![Update Majority Report Live json](https://github.com/rustymyers/majority_report_code/actions/workflows/python-app.yml/badge.svg)](https://github.com/rustymyers/majority_report_code/actions/workflows/python-app.yml)

Uses YouTube RSS feed to get MR Live episodes to derive Fun Half links. Fun Half links are stored in json for each day, updated at 12:35 PM EST with a GitHub Action. 

The GitHub Action runs the scripts and writes changes to the json back to the master branch. This provides an automatically updated json for MR Live youtube links at the staic link:

[https://raw.githubusercontent.com/rustymyers/majority_report_code/main/fun_half.json](https://raw.githubusercontent.com/rustymyers/majority_report_code/main/fun_half.json)

# Use the json

The json can be used to get the latest episodes. Each episode is added as a new entry in the `feed_links` array. This includes the URL for the private `fun_link` and `link` for the main eposide's public show on youtube. The `summary`, `title`, and `published_date` come from the main episode's rss feed. The `published_date` is used as the identifier in the code, adding episodes that do not exist already.

Json format:
```
{
feed_links: [
  fun_link: ''
  link: ''
  summary: ''
  published_date: ''
  title: ''
]
feed_name: ''
feed_url: ''
}
```

## Python3 Examples

Get the json as `data`:
```
import json
import urllib.request
with urllib.request.urlopen("https://raw.githubusercontent.com/rustymyers/majority_report_code/main/fun_half.json") as url:
  data = json.load(url)
```
With the data, you can get the latest entry using:
```
print(data["feed_links"][-1:][0])
```
Get the length of the links:
```
print(len(data["feed_links"]))
```
Print the latest Fun Half url:
```
print(data["feed_links"][-1:][0]["fun_link"])
```
