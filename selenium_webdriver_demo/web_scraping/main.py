from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates_list = []
names_list = []

#fetch event dates
dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
for date in dates:
    dates_list.append(date.text)

#fetch event names
names = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
for name in names:
    names_list.append(name.text)

#create events dict
upcoming_events = {}
for i in range(0, len(dates_list)):
    upcoming_events[i] = {
        "date": dates_list[i],
        "name": names_list[i],
        }

print(upcoming_events)

driver.quit()