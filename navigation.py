import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(executable_path="/home/onkar/PycharmProjects/pythonProject/chromedriver")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
