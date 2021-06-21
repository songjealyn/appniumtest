# -*- coding: utf-8 -*-
# @Time :2021/6/7 15:56
# @Author :song
# @Email :2697013700@qq.com
# @File :test_003_perform.py
#九宫格解锁
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
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
#九宫格元素
ele=driver.find_element_by_id("com.android.systemui:id/lockPatternView")
#起点坐标
p0=ele.location
#元素大小
size=ele.size
#步长
step=size["width"]/6
#滑屏动作z字形解锁
ta=TouchAction(driver)
ta.press(x=p0["x"]+step,y=p0["y"]+step).wait(100).\
    move_to(x=p0["x"]+3*step,y=p0["y"]+step).wait(100).\
    move_to(x=p0["x"]+5*step,y=p0["y"]+step).wait(100).\
    move_to(x=p0["x"]+3*step,y=p0["y"]+3*step).wait(100).\
    move_to(x=p0["x"]+step,y=p0["y"]+5*step).wait(100).\
    move_to(x=p0["x"]+3*step,y=p0["y"]+5*step).wait(100).\
    move_to(x=p0["x"]+5*step,y=p0["y"]+5*step).wait(100).\
    release()
ta.perform()

