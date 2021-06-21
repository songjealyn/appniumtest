# -*- coding: utf-8 -*-
# @Time :2021/6/15 15:42
# @Author :song
# @Email :2697013700@qq.com
# @File :test_008_webview.py
#h5页面
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
desired_caps={
    #平台类型
    "platformName": "Android",
    #平台版本号
    "platformVersion": "7.1.2",
    #设备名称
    "deviceName": "HUAWEI MLA-AL10",
    #是否重置
    "noReset": True,  # 不重置
    # app-包名
    "appPackage": "com.lemon.lemonban",
    #app入口activity
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("全程班")')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_android_uiautomator('new UiSelector().text("全程班")').click()
#等待Webview元素出现-html
loc1=(MobileBy.CLASS_NAME,'android.widget.LinearLayout')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc1))
time.sleep(1)
#xontext 原生控件
#先累出所有context
cons=driver.contexts
#切换至webview
driver.switch_to.context(cons[-1])
#切换后当前的操作对象;html页面
#等待元素可见
loc2=(MobileBy.XPATH,'//button[@class="bottom-btn js-report-link apply"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc2))
driver.find_element_by_xpath('//button[@class="bottom-btn js-report-link apply"]').click()