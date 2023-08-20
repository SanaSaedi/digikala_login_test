from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://digikala.com/')

time.sleep(2)

profile_button = driver.find_element(By.XPATH, '//button[@data-cro-id="header-profile"]')

profile_button.click()

time.sleep(2)

username_input = driver.find_element(By.XPATH, '//input[@name="username"]')

username_input.send_keys('09197534604')

time.sleep(2)

login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

login_button.click()

time.sleep(2)

# buttons = driver.find_elements(By.TAG_NAME, 'button')

# button_login_by_password = buttons[0]

# button_login_by_password.click()

# time.sleep(2)

password_input = driver.find_element(By.XPATH, '//input[@name="password"]')

password_input.send_keys('66632171')

submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

submit_button.click()

time.sleep(2)

# verify login was successful

profile_button = driver.find_element(By.XPATH, '//div[@data-cro-id="HP-profile-header"]')

profile_button.click()


profile = driver.find_element(By.XPATH, '//a[@data-cro-id="header-profile-detail"]')

if profile.text == 'ثنا ساعدی' :
    print('test passed')
else:
    print('test failed')


time.sleep(25)
