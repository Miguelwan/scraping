# -*- coding: utf-8 -*-
#small script to get text from a pastebin link
"""
Created on Mon Jan  4 18:24:21 2021

@author: Miguel
"""
import requests
from bs4 import BeautifulSoup

url = 'https://pastebin.com/Mfc9txQV'
headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
key = soup.find("textarea", "textarea")
print(key.text)






