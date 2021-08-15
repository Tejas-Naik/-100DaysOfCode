import time
from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')
sign_in_button = driver.find_element_by_link_text('Sign in')
sign_in_button.click()

email = driver.find_element_by_css_selector('.form__input--floating input')
email.send_keys('rntejas2005@gmail.com')

password = driver.find_element_by_css_selector('.form__input--floating #password')
password.send_keys('RN_Tejasprogrammer')

sign_in_button = driver.find_element_by_css_selector('.login__form_action_container button')
sign_in_button.click()

