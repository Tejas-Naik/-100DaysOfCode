from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://google.com/')
search_box = driver.find_element_by_name('q')
search_box.send_keys('DLS news today')
search_box.send_keys(Keys.ENTER)

video_link = driver.find_element_by_class_name('WpKAof')
video_link.click()

# search_button = driver.find_element_by_name('btnK')
# search_button.click()


# search_box = driver.find_element_by_name('search_query')
# search_box.send_keys('DLS news today')
# search_button = driver.find_element_by_id('search-icon-legacy')
# search_button.click()
# video = driver.find_element_by_class_name('style-scope ytd-video-renderer')
# video.click()
