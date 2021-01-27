import urllib.request
from bs4 import BeautifulSoup
import re

url = "http://www.haiku-data.jp/"
url += urllib.parse.quote(
    "index.php?next_i=3&&search_type=or&kigo=冬&author_name=&first5=&last5=&keyword=&submit_or=追加検索&database=現代俳句協会「現代俳句データベース」&mode=",
    safe=".?=_&")

req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
topicsindex = soup.find_all(href=re.compile("^work_detail"))
# topics = topicsindex.find_all('li')
for topic in topicsindex:
    print(topic.contents[0])  # .find('a'))  # .contents[0])
