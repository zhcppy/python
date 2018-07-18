from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Firefox()
# browser = webdriver.PhantomJS()
browser.get("https://www.baidu.com")
print(browser.current_url)
print("hello")
