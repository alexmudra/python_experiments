from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

dr= webdriver.Chrome()
dr.get("http://www.dzo.byustudio.in.ua/")
print('This is site title:', dr.title)
dr.implicitly_wait(30)

dr.find_element_by_class_name('authBtn').click()




dr.close()
dr.quit()