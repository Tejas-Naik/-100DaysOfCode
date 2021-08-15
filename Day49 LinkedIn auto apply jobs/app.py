import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_driver_path = 'C:\\Development\\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.maximize_window()
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()

# Login
email = driver.find_element_by_name('session_key')
email.send_keys('RNTejas2005@gmail.com')
password = driver.find_element_by_name('session_password')
password.send_keys('RN_Tejasprogrammer')
password.send_keys(Keys.ENTER)

# # Aplly
# time.sleep(5)
# apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
# apply_button.click()

time.sleep(5)
first_result = driver.find_element_by_css_selector(
    '.jobs-search-results ul li')
first_result.click()

time.sleep(5)
jobs_apply_button = driver.find_element_by_css_selector(
    '.jobs-apply-button--top-card button')
jobs_apply_button.click()

actions = ActionChains(driver) 
actions.send_keys(Keys.TAB * 3)
actions.send_keys(Keys.ENTER)
actions.send_keys('i')
actions.send_keys('i')
actions.send_keys(Keys.ENTER)
actions.perform()

phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys('8151039620')

next_button = driver.find_element_by_class_name('artdeco-button__text')
next_button.click()