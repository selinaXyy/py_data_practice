from selenium import webdriver
from selenium.webdriver.common.by import By #import By class

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions() #other browser options also avaliable
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) #selenium knows how to work with the latest version of these different browsers, by switching up its driver
driver.get("https://www.amazon.com") #check Security & Privacy if you are using a mac, for authorization

## demo
# price_dollar = driver.find_element(By.CLASS_NAME, value="thisIsClassName").text --> selenium object is returned so you want to specify the desired target
# query_bar = driver.find_element(By.NAME, value="q")
    # query_bar.tag_name
    # query_bar.get_attribute("placeholder")
# link = driver.find_element(By.CSS_SELECTOR, value=".className a").text

# XPath:
# demo_item = driver.find_element(By.XPATH, value='XPathCopied') #inspect->Copy->Copy XPath (change quotation marks if needed)
# you can 'find_element()' && 'find_elements()'

# driver.close() --> closes a single tab
# driver.quite() --> quite the entire browser