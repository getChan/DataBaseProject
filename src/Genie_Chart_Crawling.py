from bs4 import BeautifulSoup as bs
import requests

r = requests.get('http://www.genie.co.kr/chart/top200?ditc=D&ymd=20181010&rtm=Y&hh=13')


def getData(ymd, hour, pagenum):
    url = 'http://www.genie.co.kr/chart/top200?ditc=D&ymd=20'+ymd+'&rtm=Y&hh='+hour+'&pg='+pagenum
    with requests.get(url) as r:
        r.encoding = 'UTF-8'
        html = r.text
        soup = bs(html, 'html.parser')
        listbody = soup.find('tbody')
        songranks = listbody.find_all('td',{'class':'number'})
        titles = listbody.find_all('a', {'class':'title ellipsis'})
        artists = listbody.find_all('a', {'class':'artist ellipsis'})
        
        songrank = map(lambda x: ''.join(x.text.split()[0]), songranks)
        rankwave = map(lambda x: ''.join(x.text.split()[-1]), songranks)
        titles = map(lambda x: ''.join(x.text.split()), titles)
        artists = map(lambda x: ''.join(x.text.split()), artists)
        for song in zip(songrank, titles, artists, rankwave):
            yield song
    pass

