from selenium import webdriver
import time

chrome_driver_path = 'C:\\Development\\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.appbrewery.co/p/newsletter')

login_button = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a")
login_button.click()
time.sleep(3)

email = driver.find_element_by_name('user[email]')
email.send_keys('rntejas2005@gmail.com')

password = driver.find_element_by_name('user[password]')
password.send_keys('RN_Tejasprogrammer')
time.sleep(3)

login_btn = driver.find_element_by_name('commit')
login_btn.click()

time.sleep(3)

driver.quit()

