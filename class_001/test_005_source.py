# -*- coding: utf-8 -*-
# @Time :2021/6/8 13:27
# @Author :song
# @Email :2697013700@qq.com
# @File :test005_source.py
#列表滑动
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
desired_caps={
    "automationName":"UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "HUAWEI MLA-AL10",
    "noReset": True,  # 不重置
    # app-包名
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#获取整个屏幕
device_size=driver.get_window_size()


old_page=None
new_page=driver.page_source

while old_page!=new_page:
    loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("题库")')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
    except:
        driver.swipe(device_size["width"]*5,device_size["height"]*0.9,device_size["width"]*0.5,device_size["height"]*0.7,200)
        old_page=new_page
        new_page=driver.page_source
    else:
        driver.find_element(*loc).click()
        break
