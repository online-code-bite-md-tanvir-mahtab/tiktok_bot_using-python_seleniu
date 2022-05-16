from itertools import count
from random import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as auto
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd



web_driver_path = 'chromedriver.exe'
website_url_endpoint_second = 'https://www.tiktok.com/foryou?lang=en'
website_url_endpoint = 'https://www.tiktok.com/login'


# creating the driver
class WebElementBot:


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=web_driver_path)
        self.driver.maximize_window()
        self.driver.get(url=website_url_endpoint)
        self.driver.implicitly_wait(3)
        self.action = ActionChains(self.driver)
        sleep(3)
        # self.login_user()



    
    # now to hendle the edition of the profile
    def edit_profile(self):
        sleep(2)
        try:
            profile = self.driver.find_element_by_class_name('tiktok-1igqi6u-DivProfileContainer')
            self.action.move_to_element(to_element=profile).perform()
            sleep(3)
            
            profile = self.driver.find_element_by_link_text('View Profile')
            self.action.move_to_element(profile).click().perform()
        except:
            # x_position,y_positionn = auto.position()
            # print(x_position)
            # print(y_positionn)
            # 1526
            # 251
            x_position = 1526
            y_position = 251
            auto.moveTo(x=x_position,y=y_position)
            auto.click()



    def upload_image(self):
        sleep(4)
        edit = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button')
        sleep(2)
        edit.click()
        sleep(4)
        upload = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[2]/div[1]/div[2]/div[2]/input')
        sleep(3)
        upload.send_keys('F://python practice/tiktok-bot/tanvir.jpg')
        print("uploaded ")
        apply = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[4]/div[3]/button[2]')
        sleep(3)
        apply.click()
        try:
            username = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[2]/div[2]/div[2]/input')
            sleep(2)
            username.clear()
            sleep(2)
            username.send_keys('tanvircodder')
        except:
            pass
        
        sleep(3)
        name = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[2]/div[3]/div[2]/input')
        sleep(2)
        name.clear()
        sleep(2)
        name.send_keys('MD TANZINNUR ISLAM')
        sleep(3)
        bio = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[2]/div[4]/div[2]/textarea')
        sleep(2)
        bio.clear()
        sleep(2)
        bio.send_keys("hello everyone i am a professional android developer and python programmer")
        sleep(4)
        save = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div[3]/button[2]')
        sleep(2)
        save.click()
        sleep(3)
        try:
            save_name = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div[2]/div/div/button[2]')
            sleep(2)
            if save_name.is_displayed():
                save_name.click()
            else:
                pass
        except:
            pass

        sleep(10)
        # self.driver.back()
        sleep(3)



    def upload_vedio_or_content(self):
        sleep(20)
        try:
            upload_icon = self.driver.find_elements_by_class_name('tiktok-rpdue5-StyledUploadIcon')
            sleep(2)
            self.action.move_to_element(upload_icon).click().perform()
        except:
            auto.moveTo(x=1440,y=183)
            auto.click()
        sleep(20)
        try:
            video_upload = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div')
            sleep(2)
            video_upload.send_keys('F://python practice/tiktok-bot/bot.mp4')
            sleep(3)
            caption = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div')
            sleep(2)
            caption.send_keys("My first video")
        except:
            auto.moveTo(x=494,y=660)
            auto.click()
            sleep(40)
            post = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[7]/div[2]/button')
            sleep(2)
            if post.is_displayed():
                post.click()
                sleep(2)
        # TODO: NOT DONE PLEASE ADD



    def share_profile(self):
        sleep(3)
        share = self.driver.find_element_by_xpath(xpath='/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]')
        sleep(2)
        self.action.move_to_element(share).perform()
        sleep(10)
        x_position = 825
        y_position = 412
        auto.moveTo(x=x_position,y=y_position)
        auto.click()
        sleep(10)
        windows = self.driver.window_handles
        if len(windows) > 0:
            self.driver.switch_to(windows[1])
            texarea = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div/form/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/textarea')
            sleep(3)
            texarea.send_keys("This is my tiktok profile")
            sleep(3)
            button = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div/form/div[3]/div[2]/table/tbody/tr/td/button[2]')
            sleep(2)
            button.click()
            self.driver.close()
        else:
            self.driver.back()

        



    def login_user(self):
        sleep(3)
        # login-title-1FcQm"

        try:
            data = pd.read_csv('database.csv')
            user_name = data['user_name'][0]
            user_password = data['user_password'][0]
            # /html/body/div[2]/div/div[2]/div/div/div[3]
            # login = self.driver.find_element_by_xpath(xpath='/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]')
            # login = self.driver.find_elements_by_class_name('channel-item-wrapper-2gBWB')[2]
            login = self.driver.find_element_by_link_text('Continue with Facebook')
            login.click()
            current = self.driver.window_handles
            # now i am going to switch to the newly opend login window using seleniu
            self.driver.switch_to.window(self.driver.window_handles[1])
            sleep(3)
            phoen_number = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
            phoen_number.send_keys(user_name)
            sleep(2)
            password = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
            password.send_keys(user_password)
            sleep(2)
            login_click = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
            login_click.click()
            sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])
            print("Login is Success Performing other tasks!!")
            sleep(10)
            self.solving_the_captch()
            # /html/body/div[4]/div/div[2]/div/div[3]
        except:
            # x_position,y_position = auto.position()
            # print(x_position,y_position)
            x_position =980 
            y_position =609
            auto.moveTo(x=x_position,y=y_position)
            auto.leftClick()
            self.driver.switch_to.window(self.driver.window_handles[1])
            sleep(3)
            phoen_number = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
            phoen_number.send_keys('01955005706#@')
            sleep(2)
            password = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
            password.send_keys('01955005706#@tan')
            sleep(2)
            login_click = self.driver.find_element_by_xpath(xpath='/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
            login_click.click()
            sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])
            print("Login is Success Performing other tasks!!")
            sleep(10)
            # secsdk_captcha_refresh--text
            self.solving_the_captch()
            




    def do_folow(self):
        sleep(2)
        folowing_list = self.driver.find_elements_by_class_name('tiktok-133zmie-DivLink')
        for i in range(len(folowing_list)):
            def inner_solution():
                try:
                    folow_button = self.driver.find_element_by_xpath(xpath='/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button')
                    if folow_button.is_displayed():
                        folow_button.click()
                        sleep(5)
                        self.driver.back()
                except:
                    self.driver.refresh()
                    sleep(5)
                    self.driver.back()
            try:
                print(f"for the position :{i} is starting")
                sleep(5)
                folowing_list[i].click()
                sleep(3)
                inner_solution()
                print(f"for the postion : {i} is done")
            except:
                self.driver.refresh()
                sleep(5)
                print(f"for the position :{i} is starting")
                folowing_list[i].click()
                sleep(3)
                inner_solution()
                print(f"for the postion : {i} is done")


    def register_user(self):
        pass


    # this will search the name of the ticktoker
    def search_to_name(self):
        # self.driver.get(url=website_url_endpoint_second)
        sleep(10)
        import pyautogui as auto
        x = 479
        y = 204
        auto.moveTo(x=x,y=y)
        auto.click()
        sleep(3)
        search = self.driver.find_element_by_xpath(xpath='/html/body/div[2]/div[1]/div/div[1]/div/form/input')
        sleep(2)
        search.click()
        search.send_keys("Programming")
        sleep(2)
        button = self.driver.find_element_by_css_selector(' .tiktok-3n0ac4-ButtonSearch ')
        button.click()
        sleep(3)
        see_more = self.driver.find_element_by_xpath(xpath='/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/p[2]')
        sleep(2)
        see_more.click()
        sleep(3)
        self.solving_the_captch()
        sleep(3)
        



    # this will hendle the cpatcha
    def solving_the_captch(self):
        from selenium.webdriver.common.action_chains import ActionChains
        import random
        sleep(2)
        try:
            is_captcha_visible = self.driver.find_element_by_class_name('captcha-disable-scroll')
            count = 0
            while is_captcha_visible.is_displayed():
                print("Captcha is shown")
                if count > 5:
                    try:
                        print("limit crosed please refrese")
                        sleep(2)
                        refresh = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div/div[4]/div/a[1]/span[2]')
                        sleep(1)
                        refresh.click()
                        count = 0
                    except:
                        refresh = self.driver.find_element_by_class_name('secsdk_captcha_refresh--text')
                        sleep(2)
                        refresh.click()
                        print("the element is wrong")
                        pass
                else:
                    try:
                        print("limit crosed please refrese")
                        sleep(2)
                        refresh = self.driver.find_element_by_xpath(xpath='/html/body/div[10]/div/div[4]/div/a[1]/span[2]')
                        sleep(1)
                        refresh.click()
                        count = 0
                    except:
                        refresh = self.driver.find_element_by_class_name('secsdk_captcha_refresh--text')
                        sleep(2)
                        refresh.click()
                        print("the element is wrong")
                        pass
                
                try:
                    # we have to find the slider pice 
                    solution_peice = self.driver.find_element_by_class_name('captcha_verify_img_slide')
                    # solution_peice.click()
                    if solution_peice.is_displayed():
                        print("Found")
                        ac = ActionChains(self.driver)
                        ac.move_to_element(solution_peice)
                        ac.click_and_hold(solution_peice)
                        xofffset = 0
                        while xofffset < 240:
                            xmove = 10
                            print(xmove)
                            ymove = random.randint(-1,1)
                            ac.move_by_offset(xmove,ymove)
                            xofffset += xmove
                        ac.release()
                        ac.perform()
                        sleep(3)
                    else:
                        print("The drop slide wasnt found")
                    print("The captcha performed complete ")
                except:
                    break
                count +=1
            else:
                print("Not found")
        except:
            pass


    # '''this is will collect all the name of the tiktoker and store in a file
    # and it will click the love button for each video'''
    def newsfeed_checker(self):
        sleep(3)
        self.driver.find_element_by_class_name('tiktok-1o0yumu-DivXMarkWrapper').click()
        sleep(3)
        count = 0
        while True:
            if count != 15:
                newses = self.driver.find_elements_by_class_name('tiktok-10gdph9-DivContentContainer')
                for i in range(len(newses)):
                    print(i)
                    text = newses[i].find_element_by_tag_name('span').text
                    print(text)
                    love = newses[i].find_element_by_xpath(xpath='/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[1]')
                    sleep(2)
                    love.click()
                    print('Done')
                self.driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")
                # print(len(newses))
                sleep(3)
            else:
                break





    def close_the_driver(self):
        self.driver.close()
        self.driver.quit()



# calling the object of the class
# obj = WebElementBot()
# obj.login_user()
# # obj.edit_profile()
# # obj.upload_image()
# # obj.search_to_name()
# # obj.do_folow()
# # obj.newsfeed_checker()

# obj.upload_vedio_or_content()
