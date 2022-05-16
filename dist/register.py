from time import sleep
import click
from selenium import webdriver
import pyautogui as auto

web_driver_path = 'chromedriver.exe'
web_sign_up_url_enpoint = 'https://www.tiktok.com/signup'
class SignUp:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=web_driver_path)
        self.driver.get(url=web_sign_up_url_enpoint)
        self.driver.maximize_window()


    def register(self):
        sleep(10)
        try:
            facebook = self.driver.find_elements_by_xpath(xpath='/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]')
            sleep(3)
            facebook.click()
            sleep(5)
        except:
            # x,y = auto.position()
            # print(x,y)
            auto.moveTo(x=989,y=537)
            auto.click()
            sleep(30)

        self.driver.close()


obj = SignUp()
obj.register()