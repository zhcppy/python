import requests
import threading
import time

from requests import HTTPError


def get_one_page(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'SINAGLOBAL=8172399132158.386.1553249816410; Ugrow-G0=ea90f703b7694b74b62d38420b5273df; '
                  'SSOLoginState=1556104069; YF-V5-G0=7fb6f47dfff7c4352ece66bba44a6e5a; _s_tentry=-; '
                  'Apache=8045612219843.05.1556104075115; '
                  'ULV=1556104075150:4:3:3:8045612219843.05.1556104075115:1555897422245; ALF=1588139683; '
                  'SCF=AukolY8F9OWf8purOxy74bBPF2-LXZFm7Fhf4kaBDK8j7uauvr6yqpCUfVlCPzHyb0WW5oncdMPNj-cDc5lt9E8.; '
                  'SUHB=0d4O4QXTPc49vU; UOR=,,www.linuxde.net; '
                  'SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFBULkwKu61bgrXzaFsw_yW; '
                  'login_sid_t=401d857390ec2841e369918286b5e4f6; cross_origin_proto=SSL; wb_view_log=2560*14402; '
                  'SUB=_2AkMrj1cJf8NxqwJRmP4XyWriZIRwyAnEieKd06bSJRMxHRl-yj83ql4QtRB6AA955oJHEe4uMM7a8wHOn1zypcMD8Eco'
                  '; YF-Page-G0=da1eb9ea7ccc47f9e865137ccb4cf9f3|1557388062|1557388062',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 '
                      'Safari/537.36',
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
    except ConnectionError:
        print('error', 'ConnectionError', resp.raise_for_status())
    except HTTPError:
        print('error', 'ConnectionError', resp.raise_for_status())
    else:
        resp.close()
    return None


class MyThread(threading.Thread):

    def __init__(self, thread_nam):
        super(MyThread, self).__init__(name=thread_nam)

    def run(self) -> None:
        data = get_one_page('https://weibo.com/p/1005053325704142/photos?type=video#place')
        print('========>', data)


if __name__ == '__main__':
    now = time.time()
    for num in range(1, 30):
        thread = MyThread(num)
        thread.start()
        thread.join()
        print('========>', 'start thread success')

    print("end", time.time() - now)
