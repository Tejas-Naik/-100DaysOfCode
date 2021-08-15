from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'wrajendranaik1771@gmail.com'
TWITTER_PASSWORD = 'tejwrajsej1771'
chrome_driver_path = 'C:\\Development\\chromedriver.exe'


class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.up = up
        self.down = down

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element_by_class_name('start-text')
        go_button.click()
        time.sleep(60)
        self.current_up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.current_down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(self.current_up.text)
        print(self.current_down.text)
        
    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot(150, 50)
bot.get_internet_speed()


