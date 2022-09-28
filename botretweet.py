# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:56:37 2020

@author: 91950
"""



from selenium import webdriver
import selenium.webdriver.common.keys as k
import time as t
import pyautogui

driver=webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("https://www.twitter.com")

login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
login.click()

user = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
user.send_keys("mailid")

password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys("password")

password.send_keys(k.Keys.ENTER)

search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
search.send_keys("#IndiaAgainstNaxals")
search.send_keys(k.Keys.ENTER)

trend = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
trend.send_keys('#IndiaAgainstNaxals')
trend.send_keys(k.Keys.ENTER)

retweet = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div')
retweet.click()


        
