# http 请求库
import requests
# from requests.exceptions import RequestException
import json
import lxml
from bs4 import BeautifulSoup


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.text
    return None


def parse_noe_page(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title.string)
    print(type(soup.title))
    print(soup.body.find_all(class_='container'))
    for i, chid in enumerate(soup.body.children):
        print(i, chid.attrs)


def write_to_file(content):
    with open('data.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def run():
    url = 'https://weibo.com/p/1005053325704142/photos?type=video#place'
    html = get_one_page(url)
    if html is None:
        print("----- END -----")
    else:
        parse_noe_page(html)


if __name__ == '__main__':
    run()
