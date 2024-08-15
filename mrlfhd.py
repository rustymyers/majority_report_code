#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# --------------------------------------------------------------------------------------------------
# -- Majority Report Live Fun Half Downloader
# --------------------------------------------------------------------------------------------------
# Program    : mrlfhd.py
# To Complie : n/a
#
# Purpose    :
#
# Called By  :
# Calls      :
#
# Author     : Rusty Myers <rustymyers@gmail.com>
# Based Upon :
#
# Note       :
#
# Revisions  :
#           %Y-%m-%d <rustymyers>   Initial Version
#
# Version    : 1.0
# --------------------------------------------------------------------------------------------------
import re
import feedparser
from datetime import datetime, date
import json


def createJson(_path: str, _data={}):
    # Open the file in write mode ('w') and use 'json.dump' to write the data
    with open(_path, "w") as json_file:
        json.dump(_data, json_file)
    print(f"JSON data has been created at {_path}")


def writeJson(_path, _data: str):
    # Specify the file path where you want to write the JSON data
    # Open the file in write mode ('w') and use 'json.dump' to write the data
    with open(_path, "w") as json_file:
        json_file.write(json.dumps(_data, indent=4, sort_keys=True))
    print(f"JSON data has been written to {_path}")


def readJson(_file: str):
    try:
        # Open the file in read mode ('r') and use 'json.load' to read the data
        with open(_file, "r") as json_file:
            data = json.load(json_file)
            print("JSON data read successfully")
            return data
    except FileNotFoundError:
        print(f"File not found: {_file}")
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")


def isItToday(check_date):
    parsed_check_date = datetime.strptime(check_date, "%Y-%m-%dT%H:%M:%S%z")
    today_date = date.today()
    parsed_date = parsed_check_date.date()
    if parsed_date == today_date:
        return True
    return True


def getentries(_feed):
    entries = []
    for entry in _feed.entries:
        # mr_live = re.findall(".*MR Live.*", entry.title)
        # Video titles don't have MR Live, so can't determine
        # which ones to check with title. Disabled
        # if len(mr_live):
        publish_date = entry.published
        # print(publish_date)
        video_link = entry.link
        entry_title = entry.title
        summary_text = entry.summary
        print(summary_text[:95])
        url_regex = "[Ff][Uu][Nn] [hH][aA][lL][fF].*(https:\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])"
        try:
            urls = re.findall(url_regex, summary_text, flags=re.IGNORECASE)
        except:
            print("Unable to regex. No links?")
            continue
        print(urls)
        if not len(urls):
            # print("No Fun Half Link")
            continue
        else:
            fun_half = urls[0]
        entry_json = {
            "link": video_link,
            "fun_link": fun_half,
            "published_date": publish_date,
            "title": entry_title,
            "summary": summary_text,
        }
        entries.append(entry_json)
    return entries


# Open the file of current fun halfs
fun_half_json = readJson("fun_half.json")

# Get videos from feed
headers = {"User-Agent": "Mozilla"}
channel_id = "UC-3jIAlnQmbbVMV6gR7K8aQ"
url = "https://www.youtube.com/feeds/videos.xml?channel_id={0}".format(channel_id)
feed = feedparser.parse(url)

print("Feed Title:", fun_half_json["feed_name"])
print("Feed Link:", fun_half_json["feed_url"])
print(feed)
fun_halfs = getentries(feed)
new_shows = False
for fun_half_entry in fun_halfs:
    feed_date = fun_half_entry["published_date"]
    parsed_feed_date = datetime.strptime(feed_date, "%Y-%m-%dT%H:%M:%S%z")
    update_entry = True
    for entry in fun_half_json["feed_links"]:
        entry_date = entry["published_date"]
        parsed_entry_date = datetime.strptime(entry_date, "%Y-%m-%dT%H:%M:%S%z")
        if parsed_feed_date.date() == parsed_entry_date.date():
            update_entry = False
    if update_entry:
        print("Adding {0}".format(fun_half_entry["title"]))
        fun_half_json["feed_links"].append(fun_half_entry)
        new_shows = True
if new_shows:
    writeJson("fun_half.json", fun_half_json)
