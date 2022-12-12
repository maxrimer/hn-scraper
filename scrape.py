import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')


def sort_news_list(hnlist):
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)


def create_hn(links, subtext):
    hn = []
    for id, val in enumerate(links):
        title = val.getText()
        href = val.find('a').get('href')
        votes = subtext[id].select('.score')
        if votes:
            points = int(votes[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn


pprint(sort_news_list(create_hn(links, subtext)))
