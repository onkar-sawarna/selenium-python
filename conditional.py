from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("http://demo.guru99.com/test/newtours/")
ele=driver.find_element_by_name("userName")
print(ele.is_displayed())
print(ele.is_enabled())
pwd_ele=driver

