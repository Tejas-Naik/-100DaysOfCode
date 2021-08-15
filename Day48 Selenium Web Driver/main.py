from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# we are going to make amazon price detector
driver.get('https://www.python.org/')
# driver.get('https://www.amazon.in/Puma-Unisex-Rebound-Sneakers-7-36957301_7/dp/B07KG1LJ4Z/ref=sr_1_14?dchild=1&pf_rd_i=22953310031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=5b0ba12e-1928-4f57-9083-0ce925d8b783&pf_rd_r=4R9BE97B7QHCP1HFAHF2&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1615079455&refinements=p_89%3APuma&rnid=3837712031&s=apparel&sr=1-14')  # url of the product
############################################ Ways of FINDING elements ##############################################################
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)  # we have to print the text because it returns a function

# name = driver.find_element_by_name('q')
# print(name.get_attribute('placeholder'))

# python_logo = driver.find_element_by_class_name('python-logo')
# print(python_logo.size)

# documentation_link = driver.find_element_by_css_selector('.documentation-widget a')
# print(documentation_link.text)

submit_website_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_website_link.text)

driver.close()
"""
    .close() closes the current tab
    .quit() closes the existing window
"""
