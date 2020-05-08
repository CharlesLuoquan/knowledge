"""
爬取豆瓣电影TOP250 - 完整示例代码
"""
import codecs
import requests
import logging
from bs4 import BeautifulSoup

logging.captureWarnings(True)
download_url="https://movie.douban.com/top250"

def download_page(url):
    data=requests.get(url, verify=False).content
    return data

def parse_html(html):
    soup=BeautifulSoup(html)
    movie_list_soup=soup.find('ol', attrs={'class':'grid_view'})

    movie_name_list=[]

    for movie_li in movie_list_soup.find_all('li'):
        detail =movie_li.find('div', attrs={'class':'hd'})
        movie_name = detail.find('span', attrs={'class':'title'}).getText()

        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, download_url + next_page['href']
    return movie_name_list, None

def main():
    #print(download_page(download_url))
    url=download_url

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()