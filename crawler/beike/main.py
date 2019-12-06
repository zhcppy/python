import logging
import time
import pymongo
from datetime import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

WEB_BASE_URL = 'https://sz.zu.ke.com'

ZU_FANG = WEB_BASE_URL+'/zufang/rs/'


class BeiKe:

    def __init__(self):
        # which chromedriver
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = client['beike']

    def get_house_info(self, url=ZU_FANG):
        # self.driver.execute_script("window.open('');")
        # time.sleep(1)
        # self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles) - 1])

        url = '%s?unique_id=%s%s%d' % (url, '29d3aaaa-f8b7-494f-b5a5-21a07fecea9c', 'zufangrs', int(round(time.time() * 1000)))
        self.driver.get(url)
        logging.debug('web title:%s', self.driver.title )

        self.driver.find_element_by_id('show_more').click()
        self.driver.execute_script('$.showSelectBuyer()')
        self.waitPageOver((By.CLASS_NAME, 'bgc'))
        self.driver.find_element_by_id('show_more').click()

        # house = {
        #     "title":
        #     "subtitle":
        #     "houseCode":
        #     "type"
        #     "area"
        #     "orient"
        # }

        # {
        #     "transactionDate":
        #     "transactionPrice"
        #     "houseType":
        #     "houseArea"
        #     "leaseWay"
        #     "rental"
        # }
        # self.driver.execute_script('$.showSelectBuyer()')
        # buyer_list = self.driver.find_element_by_id('buyer-list')
        # buyer_list_items = buyer_list.find_elements_by_tag_name('li')
        # buyer_list_items[0].click()
        # self.driver.execute_script('$.closeSelectBuyer()')
        #
        # time.sleep(1)
        # self.driver.execute_script('$.showSelectSeat()')
        # seat_list = self.driver.find_element_by_id('seat-list')
        # seat_list_items = seat_list.find_elements_by_tag_name('li')
        # seat_list_items[3].click()
        # self.driver.execute_script('$.closeSelectSeat()')
        #
        # self.driver.find_element_by_id('autoSubmit').click()
        #
        # self.driver.find_element_by_id('query_ticket').click()

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


if __name__ == '__main__':
    # 初始化日志
    logging.basicConfig(level=logging.DEBUG)

    bk = BeiKe()
    bk.get_house_info()
    # bk.scrollTo()