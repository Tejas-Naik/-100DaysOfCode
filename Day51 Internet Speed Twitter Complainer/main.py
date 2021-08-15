from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'wrajendranaik1771@gmail.com'
TWITTER_PASSWORD = 'tejwrajsej1771'
chrome_driver_path = 'C:\Development\chromedriver.exe'

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go_button.click()
        time.sleep(30)
        self.current_up = self.driver.find_element_by_css_selector(
            '.result-data .upload-speed').text
        self.current_down = self.driver.find_element_by_css_selector(
            '.result-data .download-speed').text
        print(f'{self.up} Upload')
        print(f'{self.down} Download')
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        TWEET_TEXT = f'Hey IP Why is the internet speed is tool low while you have promised to give {self.up}/{self.down} while I am only getting {self.current_up}/{self.current_down}'
        tweet.send_keys(TWEET_TEXT)
        
bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.tweet_at_provider()
