# -*- coding: utf-8 -*-
# @Time :2021/6/17 15:17
# @Author :song
# @Email :2697013700@qq.com
# @File :test_009_tencent.py
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
#启动appnium时，需要制定Chromedriver的目录，使用appnium默认路径会报错
#在切换小程序webview时，会去匹配chrome内核39的驱动，在切换完成之后，在打印所有的窗口

#小程序
desired_caps={}
#X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"]=True
desired_caps["automationName"]="UiAutomator2"
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="10"
desired_caps["deviceName"]="PCT-AL10"
desired_caps["appPackage"]="com.tencent.mm"
desired_caps["appActivity"]="com.tencent.mm.ui.LauncherUI"
desired_caps["chromedriverExecutableDir"]="D:\soft\chromedriver"
desired_caps["noReset"]=True
desired_caps["unicodeKeyboard"]=True
desired_caps["chromeOptions"]={"androidProcess":"com.tencent.mm:appbrand0"}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
wait=WebDriverWait(driver,30)
#进入微信界面
loc=(MobileBy.ID,'com.tencent.mm:id/baj')
wait.until(EC.visibility_of_element_located(loc))
driver_size=driver.get_window_size()
driver.swipe(driver_size["width"]*0.5,driver_size["height"]*0.2,driver_size["width"]*0.5,driver_size["height"]*0.9,200)
#进入微信小程序
loc=(MobileBy.ID,'new UiSelector().text("柠檬班")')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
#获取上下文
cons=driver.contexts
#切换到小程序webview
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')


