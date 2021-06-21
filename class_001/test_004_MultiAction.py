# -*- coding: utf-8 -*-
# @Time :2021/6/8 10:34
# @Author :song
# @Email :2697013700@qq.com
# @File :test_oo4_MultiAction.py
#双指拖动
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
import time
des={
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"HUAWEI",
    "noReset":True, #不重置
    #app-包名
    "appPackage":"com.baidu.BaiduMap",
    "appActivity":"com.baidu.baidumaps.WelcomeScreen"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
time.sleep(10)
driver_size=driver.get_window_size()
#向左上角滑动
a=TouchAction(driver)
a.press(x=driver_size["width"]*0.5,y=driver_size["height"]*0.5).wait(20).\
    move_to(x=driver_size["width"]*0.1,y=driver_size["height"]*0.1)
#向右下角滑动
b=TouchAction(driver)
b.press(x=driver_size["width"]*0.5,y=driver_size["height"]*0.5).wait(20).\
    move_to(x=driver_size["width"]*0.9,y=driver_size["height"]*0.9)
ma=MultiAction(driver)
ma.add(a,b)
ma.perform()