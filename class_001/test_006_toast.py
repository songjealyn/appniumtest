# -*- coding: utf-8 -*-
# @Time :2021/6/8 13:42
# @Author :song
# @Email :2697013700@qq.com
# @File :test_006_toast.py
#提示
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
loc=(MobileBy.ID,"com.lemon.lemonban:id/navigation_my")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
loc=(MobileBy.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
loc=(MobileBy.ID,"com.lemon.lemonban:id/btn_login")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
loc=(MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
try:
    WebDriverWait(driver,10,0.01).until(EC.presence_of_element_located(loc))
except:
    print("没找到")
else:
    text=driver.find_element(*loc).text
    print(text)
