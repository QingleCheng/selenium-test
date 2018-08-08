#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import urllib
import time
from datetime import datetime
import os
import win32api
import win32con
from selenium.webdriver.common.action_chains import ActionChains

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showhenStarting",True)

fp.set_preference("browser.helperApps.neverAsk.saveToDisk","applaction/octet-stream")#下载文件

#这里用有GUI界面的Firefox为例子，当然你喜欢Chome，这里换成Chrome也可以
#构造模拟浏览器
firefox_login=webdriver.Firefox(firefox_profile = fp)
#Chrome_login=webdriver.Chrome()

#打开网址
firefox_login.get('http://zrzh.iemzzs.com/oa/scriptlsit.aspx?kind=Issue&Issue_No=2017%C4%EA01%C6%DA')
firefox_login.maximize_window()#窗口最大化，可有可无，看情况
st='//*[@id="ctl00_cphContect_Dglist"]/tbody/tr['
st1=']/td/div/div[1]/a'

for i in range(2):
    file=st+str(i+1)+st1
    filename=firefox_login.find_element_by_xpath(file)
    papername=filename.text
    print (papername)
    firefox_login.find_element_by_xpath(file).click()
    firefox_login.implicitly_wait(10)  # 隐性等待30s，如果加载完成就进行下一步
    mkpath = "D:\\code\\python\\selenium_test\\"+papername+'\\'
    mkpath1 = 'D:\\code\\python\\selenium_test\\' + papername+'\\'+papername
    mkdir(mkpath)
    # fp.set_preference("browser.download.dir", mkpath1)
    # firefox_login = webdriver.Firefox(firefox_profile=fp)
    # firefox_login.find_element_by_xpath('//*[@id="pdf"]/img').click()
    # 通过ActionChains的context_click进行对link元素右键操作,在按下另存为的快捷键K
    # ActionChains(firefox_login).context_click(firefox_login.find_element_by_xpath('//*[@id="pdf"]/img')).send_keys('K').perform()
    # 右键超链接另存为
    ActionChains(firefox_login).context_click(firefox_login.find_element_by_xpath('//*[@id="pdf"]/img')).perform()
    # 延时2s
    time.sleep(2)
    # 按下K键,这里用到了win32api,win32con
    win32api.keybd_event(75, win32con.KEYEVENTF_KEYUP, 0)  # 75的含义就是键盘的K
    # os.system('test1.exe ' + mkpath1 + '.pdf')
    os.system('test1.exe ' + mkpath1 )
    # time.sleep(5)
    # firefox_login.find_element_by_xpath('//*[@id="Content"]').click()#返回上一级目录
    # firefox_login.get('http://zrzh.iemzzs.com/oa/scriptlsit.aspx?kind=Issue&Issue_No=2017%C4%EA01%C6%DA')
    click_btn = firefox_login.find_element_by_xpath('//*[@id="Content"]')  # 单击按钮
    ActionChains(firefox_login).click(click_btn).perform()  # 链式用法

# firefox_login.find_element_by_xpath('/html/body/form/div[2]/h1/div[3]/span[2]/a/img').click()
# time.sleep(10)           #设置等待时间10s
