from selenium import webdriver  
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('C:\\Users\\ajinkya.bhobad\\Desktop\\jars\\chromedriver.exe')
driver.get('https://www.google.com/')
elem = driver.find_element_by_xpath("//*[@id='lst-ib']")
elem.send_keys("testproject.io")
elem.send_keys(Keys.RETURN)
driver.close()