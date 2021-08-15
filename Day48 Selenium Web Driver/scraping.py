from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')

# the first event
# first_event = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a')
# print(first_event.text)

# second_event = driver.find_element_by_xpath(
#     '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/a')
# print(second_event.text)

# third_event = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[3]/a')
# print(third_event.text)

# forth_event = driver.find_element_by_xpath(
#     '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[4]/a')
# print(forth_event.text)

# fifth_event = driver.find_element_by_xpath(
#     '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[5]/a')
# print(fifth_event.text)

# events
# all_events = {}
# events = []
# for _ in range(1, 6):
#     events.append(driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{_}]/a'))

# dates = driver.find_elements_by_css_selector('.menu time')
# for _ in range(len(events)):
#     all_events[_] = {'name':events[_].text, 'time':dates[_].text}

# print(all_events)

event_dates = driver.find_elements_by_css_selector('.event-widget time')
event_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {{'name': event_names[_], 'time': event_dates[_]} for _ in range(len(event_dates))}
print(events)
driver.quit()
