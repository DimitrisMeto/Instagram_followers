from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "/Users/dimitris/Development/chromedriver"
SIMILAR_ACCOUNT = "joystickgrofficial"
USERNAME = "yuki_metochianaki"
PASSWORD = os.environ.get("PASSWORD")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self, driver_path, driver_options):
        self.driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    def log_in(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, "li a._a6hd")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        time.sleep(2)

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button._acan")
        for follow_button in follow_buttons:
            if follow_button != follow_buttons[0]:
                try:
                    follow_button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.CSS_SELECTOR, "button._a9_1")
                    cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH, options)
bot.log_in()
bot.find_followers()
bot.follow()

