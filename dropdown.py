from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element=driver.find_element(By.ID,"RESULT_RadioButton-9")
drop=Select(element)
#drop.select_by_visible_text('Morning')
#drop.select_by_index(2)
drop.select_by_value("Radio-2")
#capture all the options and print them as output
print(len(drop.options))
all_options=drop.options
for option in all_options:
    print(option.text)
driver.close()