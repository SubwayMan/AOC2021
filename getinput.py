import requests
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
import json
import os, sys

load_dotenv()

year, day, out = sys.argv[1:]
url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)

headers = CaseInsensitiveDict()
headers["cookie"] = os.environ.get("session")

data = requests.get(url, headers=headers)
print(data.text)

outfile = open(out, "w")
outfile.write(data.text)
outfile.close()
