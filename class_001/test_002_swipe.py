# -*- coding: utf-8 -*-
# @Time :2021/6/7 13:26
# @Author :song
# @Email :2697013700@qq.com
# @File :test_002_swipe.py
#滑动
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import  MobileBy
desired_caps={
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"HUAWEI",
    "noReset":True, #不重置
    #app-包名
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
loc=(MobileBy.ID,"com.lemon.lemonban:id/mainpage_recyclerView")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
ele=driver.find_element(*loc)
ele.click()
driver_size=driver.get_window_size()
driver.swipe(driver_size["width"]*0.5,driver_size["height"]*0.9,driver_size["width"]*0.5,driver_size["height"]*0.1,200)