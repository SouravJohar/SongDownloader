from bs4 import BeautifulSoup as bs
import urllib
import requests
from urllib import re


url_slice1 = r'http://mp3clan.ws/mp3/'
url_slice2 = r'.html'
song_name = raw_input()
url = url_slice1 + song_name + url_slice2
r = requests.get(url)
soup = bs(r.content, 'lxml')
titles = soup.find_all('div', {'class': 'unselectable'})[0:max_options_limit]
download_links = soup.find_all('div', {'title': 'Download'})[0:max_options_limit]
links = []
temp_html = soup.find_all('div', {'title': 'Download'})
for j in temp_html:
    links.append(j.find('a')['href'])
choice = int(raw_input())
# Download
response = urllib.urlopen(links[choice - 1])
mp3 = response.read()
f = open("thisshouldwork.mp3", "w")
f.write(mp3)
f.close()
print "Done"
