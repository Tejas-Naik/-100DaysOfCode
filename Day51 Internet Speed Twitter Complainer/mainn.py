from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
chrome_driver_path = "C:\Development\chromedriver.exe"
EMAIL = "wrajendranaik1771@gmail.com"
PASSWORD = "tejwrajsej1771"


class InternetSpeedTwitterBot():
    def __init__(self, downlowad_speed, upload_speed):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.downlowad_speed = downlowad_speed
        self.upload_speed = upload_speed

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(20)
        #Click on the start button
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
            time.sleep(30)
        except NoSuchElementException:
            print("Couldn't click on the start button.\n" + NoSuchElementException)

        time.sleep(60)

        # Getting the results
        try:
            download = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            upload = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
            self.message = "Your message"
            self.tweet_provider() if float(download) < self.downlowad_speed or float(
                upload) < self.upload_speed else print("Internet speed is Okay now.")
        except NoSuchElementException:
            print("Couldn't get either download or upload speed\n" +
                  NoSuchElementException)

    def tweet_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div').click()
        except NoSuchElementException:
            print("Could not click on login\n" + NoSuchElementException)
        time.sleep(3)
        try:
            self.driver.find_element_by_name(
                'session[username_or_email]').send_keys(EMAIL)
            self.driver.find_element_by_name(
                'session[password]').send_keys(PASSWORD)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span').click()
        except NoSuchElementException:
            print("Could not enter keys on login / click on login button\n" +
                  NoSuchElementException)
        time.sleep(10)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(self.message)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span').click()
        except NoSuchElementException:
            print("Could not tweet.\n" + NoSuchElementException)

bot = InternetSpeedTwitterBot(150, 50)
# bot.get_internet_speed()
bot.tweet_provider()