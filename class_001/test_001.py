# -*- coding: utf-8 -*-
# @Time :2021/6/2 16:22
# @Author :song
# @Email :2697013700@qq.com
# @File :test_001.py
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

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
#1.与appnium建立连接，
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
loc=(MobileBy.ID,"com.lemon.lemonban:id/mainpage_recyclerView")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
ele=driver.find_element(*loc)
ele.click()
#设备是连接状态 -adb devices是可以识别
#appnium是启动状态