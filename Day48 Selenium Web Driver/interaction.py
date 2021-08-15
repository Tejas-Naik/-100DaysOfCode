from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_count = driver.find_element_by_css_selector('#articlecount a')
# print(article_count.text)

# search_box = driver.find_element_by_name('search')
# search_box.click()

# search_box.send_keys("Python")
# search_box.send_keys(Keys.ENTER)

# developers = driver.find_element_by_link_text('Developers')
# developers.click()

time.sleep(10)
driver.quit()
