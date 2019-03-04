from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

dr = webdriver.Chrome()
dr.get("http://www.dzo.byustudio.in.ua/cabinet")
fill_pass = dr.find_element_by_xpath("//div[@class='inp']//input[@name='email']")
fill_pass.sendKeys('sdklfjkdjsf')


print('This is site title:', dr.title)




#dr.implicitly_wait(30)
#dr.close()
#dr.quit()