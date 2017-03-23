#!/Users/Luna/.pyenv/versions/2.7.10/envs/mdev-py-2.7.10/bin/python2.7

from bs4 import BeautifulSoup
import requests

url = raw_input("url : ")
r = requests.get("http://"+url)
data = r.text
soup = BeautifulSoup(data,"lxml")

for link in soup.find_all('a'):
    print(link.get('href'))

