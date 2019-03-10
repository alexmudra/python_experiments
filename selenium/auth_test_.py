from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


dr = webdriver.Chrome()
log = ("organizator_main@byustudio.in.ua")
ps = "VNNcY7989"

dr.get("http://www.dzo.byustudio.in.ua/cabinet")
dr.find_element_by_xpath("//div[@class='inp']//input[@name='email']").send_keys(log)
dr.implicitly_wait(30)
dr.find_element_by_xpath("/html/body/div[2]/section/div/section[2]/div/section/form/section[1]/table/tbody/tr[2]/td[2]/div/input").send_keys(ps)
dr.find_element_by_xpath("/html/body/div[2]/section/div/section[2]/div/section/form/section[2]/table/tbody/tr[1]/td[2]/div/div[1]/div/button").click()
print("==========================================")
print()
print("Танюшка, дивись що ми знайшли: ))", dr.title)
print()
print("==========================================")
#assert "Кабінет - Мої закупівлі" != dr.title

dr.find_element_by_xpath("//a[contains(text(),'Поточні тендери')]").click()
dr.find_element_by_xpath("//a[contains(text(),'Створити закупівлю')]").click()
dr.find_element_by_xpath("//*[@id='tender']/section[1]/table/tbody/tr[5]/td[2]/div/div[1]/div[1]/input").send_keys(100)

#dr.close()
#dr.quit()