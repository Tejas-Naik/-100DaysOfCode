from selenium import webdriver

chrome_driver_path = 'C:\\Development\\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://python.org/')

event_times = driver.find_elements_by_css_selector('.event-widget time')
event_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {}
for i in range(len(event_times)):
    events[i] = {
        'name': event_names[i].text,
        'time': event_times[i].text
    }

print(events)

driver.quit()
