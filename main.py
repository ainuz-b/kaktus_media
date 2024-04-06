import requests
from datetime import datetime
from bs4 import BeautifulSoup as BS

today = datetime.today().date()

def get_html(URL):
    html = requests.get(URL)
    return html.text

def get_data(html):
    soup = BS(html, 'lxml')
    list_news = soup.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
    data_ = []
    count = 0
    for news in list_news:
        if count < 20:
            news_link = news.find('a', class_='ArticleItem--name').get('href')
            data_.append({
                'title': news.find('a', class_='ArticleItem--name').text,
                'photo': news.find('a', class_='ArticleItem--image').find('img').get('src'),
                'news_link': news_link
            })
            count += 1
        else:
            break

    return data_

def main():
    URL = f'https://kaktus.media/?lable=8&date={today.year}-{today.month}-{today.day}&order=time'
    print(URL)
    html_content = get_html(URL)
    data = get_data(html_content)
    return data

if __name__ == '__main__':
    main()