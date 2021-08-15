from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = 'https://www.instagram.com/python.hub/'
USERNAME = 'rntejas1771'
PASSWORD = 'tejwrajsej1771'


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        search = self.driver.find_element_by_class_name('XTCLo')
        search.send_keys('python.hub')
        python_hub_acc = self.driver.find_element_by_is('f890da94d06884')
        python_hub_acc.click()
        # id = 'f890da94d06884'

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
# bot.follow()
