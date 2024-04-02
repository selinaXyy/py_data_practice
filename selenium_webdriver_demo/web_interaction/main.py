from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #contains consts, (e.g., TAB, ENTER)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

input_fn = driver.find_element(By.NAME, value="fName")
input_ln = driver.find_element(By.NAME, value="lName")
input_email = driver.find_element(By.NAME, value="email")
btn_submit = driver.find_element(By.TAG_NAME, value="button")
# .click()
# .send_keys("keys from the keyboard that you want to send to this element", Keys.ENTER)
input_fn.send_keys("Yiyang")
input_ln.send_keys("Xue")
input_email.send_keys("selinaxue2@gmail.com")
btn_submit.click()

driver.quit()