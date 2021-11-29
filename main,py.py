import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#print(driver.page_source)
#driver.close()
driver.quit()


