# -*- coding: utf-8 -*-
# @Time :2021/6/8 16:09
# @Author :song
# @Email :2697013700@qq.com
# @File :test_007_activity.py
#切换app
import time
from appium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
desired_caps={
    "automationName":"UiAutomator2",#toast必须UiAutomator2
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "HUAWEI MLA-AL10",
    "noReset": True,  # 不重置
    # app-包名
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(5)
driver.start_activity("com.baidu.BaiduMap","com.baidu.baidumaps.WelcomeScreen")

# driver.background_app()#至于后台
# driver.activate_app()#至于前台