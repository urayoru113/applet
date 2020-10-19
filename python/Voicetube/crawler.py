import re

import requests
from bs4 import BeautifulSoup

from sqlite import Database

def fetch_text(text):
    text = re.match(r"[\n\s]*(.+\w.)[\n\s]*", text).group(1)
    text = text.replace("'", "''")
    text = text.replace("\\", "\\\\")
    return text

url = "https://tw.voicetube.com/videos/79574"
selector = '#show-caption-table tr td:last-child'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sequence = soup.select(selector)

vt = Database('voicetube.db')
vt.create('Sound_Euphonium', seq_id='integer', text='text')

for index, obj in enumerate(sequence):
    text = fetch_text(obj.text)
    vt.insert(index, text)
    print(f"save {index}, {text}")
vt.commit()
vt.close()
