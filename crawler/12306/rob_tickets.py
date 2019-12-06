"""
pip install selenium

[open download chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)
"""

import logging
import time
from datetime import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

WEB_BASE_URL = 'https://kyfw.12306.cn'

LOGIN = WEB_BASE_URL + '/otn/resources/login.html'

LEFT_TICKET = WEB_BASE_URL + '/otn/leftTicket/init'

CENTER = WEB_BASE_URL + '/otn/view/index.html'

WEB_TITLE = '中国铁路12306'

SZQ = '深圳,SZQ'
WHN = '武汉,WHN'


class RobTickets:

    def __init__(self, from_station=SZQ, to_station=WHN, date=datetime.now().strftime('%Y-%m-%d')):
        # which chromedriver
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.fromStation = from_station
        self.toStation = to_station
        self.date = date

    def home_login(self):
        self.driver.get(LOGIN)
        self.account()

    def left_ticket(self):
        self.driver.execute_script("window.open('');")
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])
        url = '%s?linktypeid=%s&fs=%s&ts=%s&date=%s&flag=%s' % (
            LEFT_TICKET, 'dc', self.fromStation, self.toStation, self.date, 'N,Y,Y')
        self.driver.get(url)
        if WEB_TITLE not in self.driver.title:
            logging.error('web title is not match')
            self.driver.quit()
        self.waitPageOver((By.CLASS_NAME, 'bgc'))
        self.driver.find_element_by_id('show_more').click()
        self.driver.execute_script('$.showSelectBuyer()')
        self.account()
        self.waitPageOver((By.CLASS_NAME, 'bgc'))
        self.driver.find_element_by_id('show_more').click()

        self.driver.execute_script('$.showSelectBuyer()')
        buyer_list = self.driver.find_element_by_id('buyer-list')
        buyer_list_items = buyer_list.find_elements_by_tag_name('li')
        buyer_list_items[0].click()
        self.driver.execute_script('$.closeSelectBuyer()')

        time.sleep(1)
        self.driver.execute_script('$.showSelectSeat()')
        seat_list = self.driver.find_element_by_id('seat-list')
        seat_list_items = seat_list.find_elements_by_tag_name('li')
        seat_list_items[3].click()
        self.driver.execute_script('$.closeSelectSeat()')

        self.driver.find_element_by_id('autoSubmit').click()

        self.driver.find_element_by_id('query_ticket').click()

    def screenshot(self):
        self.driver.save_screenshot(datetime.now().strftime('screenshot_%Y%m%d%H%M%S.png'))

    def scrollTo(self):
        self.driver.execute_script('window.scrollTo({top:document.body.scrollHeight, behavior:"smooth"});')

    def waitPageOver(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutError:
            logging.error('wait web loading time out')
            self.driver.quit()

    def account(self):
        hd_account = self.driver.find_element_by_class_name('login-hd-account')
        ActionChains(self.driver).move_to_element(hd_account).pause(1).click(hd_account).perform()
        time.sleep(1)
        username = self.driver.find_element_by_id('J-userName')
        username.clear()
        username.send_keys('ZZZDRY')
        time.sleep(0.5)
        password = self.driver.find_element_by_id('J-password')
        password.clear()
        password.send_keys('X86226zhdc')
        time.sleep(1)
        login = self.driver.find_element_by_id('J-login')
        while True:
            if 'rgba(255, 130, 1, 0.8)' in login.value_of_css_property('background'):
                logging.info('================================================')
                ActionChains(self.driver).move_to_element(login).pause(1).click(login).perform()
                time.sleep(1)
                self.driver.refresh()
                return
            else:
                time.sleep(1)
                logging.info('请选择图片正确的图片验证码，然后点击【立即登录】。。。。。。')


if __name__ == '__main__':
    # 初始化日志
    logging.basicConfig(level=logging.INFO)

    # 实例化抢票
    rt = RobTickets(SZQ, WHN, (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
    # 登录
    # rt.home_login()
    # 查询余票
    rt.left_ticket()
    # 截图
    # rt.screenshot()
    # 平滑滚动到页面底部
    # rt.scrollTo()
