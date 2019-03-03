from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr= webdriver.Chrome()
dr.get("https://habr.com/ru/post/29980/")
print('This is site title:', dr.title)


dr.find_element_by_class_name('logo')
print('Logo is available')

dr.contextMenu(dr.find_element_by_class_name('logo'))


dr.close()
dr.quit()


# Again new window
# driver.switch_to_window(driver.window_handles[1])
# print (" Facebook window should go to Google ")
# print ("New window ", driver.title)
# driver.get("http://google.com")
# print ("New window ", driver.title)
#
#
# # browser = webdriver.Firefox()
# body = browser.find_element_by_tag_name('body')
# body.send_keys(Keys.CONTROL + 'n')