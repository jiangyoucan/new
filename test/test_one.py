
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('iphone')

driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)

driver.quit()

