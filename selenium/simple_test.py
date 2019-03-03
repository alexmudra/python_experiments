from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://python-scripts.com/web-automation-with-python-and-selenium')


# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
#
# opts = Options()
# opts.set_headless()
# assert opts.headless
#
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')



# Switch to new window
# driver.switch_to_window(driver.window_handles[-1])
# print(" Twitter window should go to facebook ")
# print ("New window ", driver.title)
# driver.get("http://facebook.com")
# print ("New window ", driver.title)
#
# # Switch to old window
# driver.switch_to_window(driver.window_handles[0])
# print (" Linkedin should go to gmail ")
# print ("Old window ", driver.title)
# driver.get("http://gmail.com")
# print ("Old window ", driver.title)
#
# # Again new window
# driver.switch_to_window(driver.window_handles[1])
# print (" Facebook window should go to Google ")
# print ("New window ", driver.title)
# driver.get("http://google.com")
# print ("New window ", driver.title)
#
# #
# # browser = webdriver.Firefox()
# body = browser.find_element_by_tag_name('body')
# body.send_keys(Keys.CONTROL + 'n')