from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
#driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10) #specify once in the code and applicable for all the elements
assert "Welcome: Mercury Tours" in driver.title
#driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element(By.NAME,"userName").send_keys("mercury")
#driver.find_element_by_name("password").send_keys("mercury")
driver.find_element(By.NAME,"password").send_keys("mercury")
#driver.find_element_by_name("login").click()
driver.find_element(By.NAME,"submit").click()
driver.close()


