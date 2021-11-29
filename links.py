from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("http://demo.guru99.com/test/newtours/index.php")
links=driver.find_elements(By.TAG_NAME,"a")
print("No of links present :" ,len(links))
# for link in links:
#     print(link.text)
# driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
