from selenium import webdriver
import pretty_errors

chrome_driver_path = 'C:\\Development\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')  #"https://www.amazon.com/dp/B084KYHZRS/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B084KYHZRS&pd_rd_w=IZtOY&pf_rd_p=cbc856ed-1371-4f23-b89d-d3fb30edf66d&pd_rd_wg=Kvfha&pf_rd_r=2N2CZ6A5TR8V7QWX2F7R&pd_rd_r=362ff2e6-d71f-4fa1-9ca4-39b9885a46cd&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzM1dRTVUzMEFCUUpMJmVuY3J5cHRlZElkPUEwNTQzNjY0M0s2NTA2T0pVTzU3SSZlbmNyeXB0ZWRBZElkPUEwMTIwMzUwM1MySlYwTUxNWEFXSyZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
driver.maximize_window

# there are a lot of other ways find a certain elements 
## Finding by ID(CSS)
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

##Findinf by name this is usefyl when you are working with forms
# search_bar = driver.find_element_by_name('q') 
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute('placeholder'))

## Finding by class name
# logo = driver.find_element_by_class_name('python-logo')
# print(logo.size)

## finding element by CSS selector
# docs_link = driver.find_element_by_css_selector('.documentation-widget a')
# docs_link.click()

## Finding by link text
# developers = driver.find_element_by_link_text('Developers')
# developers.click()

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]')
print(bug_link.text)


driver.quit()
