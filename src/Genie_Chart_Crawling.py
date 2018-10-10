from bs4 import BeautifulSoup as bs
import requests

r = requests.get('http://www.genie.co.kr/chart/top200?ditc=D&ymd=20181010&rtm=Y&hh=13')
#year, month, date
ymd = '20181010'
#hour
hour = '13'
# pagenum
pagenum = '1'
url = 'http://www.genie.co.kr/chart/top200?ditc=D&ymd='+ymd+'&rtm=Y&hh='+hour+'&pg='+pagenum
with requests.get(url) as r:
    r.encoding = 'UTF-8'
    html = r.text
    soup = bs(html, 'html.parser')
    listbody = soup.find('tbody')
    songranks = listbody.find_all('td',{'class':'number'})
    titles = listbody.find_all('a', {'class':'title ellipsis'})
    artists = listbody.find_all('a', {'class':'artist ellipsis'})
    
    songranks = map(lambda x: x.text.strip(), songranks)
    titles = map(lambda x: x.text.strip(), titles)
    artists = map(lambda x: x.text.strip(), artists)
    for song in zip(songranks, titles, artists):
        print(song)
