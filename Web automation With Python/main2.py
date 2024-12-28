from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import os


from selenium.webdriver.common.by import By


# Chrome driver initialize karen
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Website ko open karen
driver.get("https://practicetestautomation.com/practice-test-login/")
user_username = driver.find_element(By.ID, 'username')
user_password = driver.find_element(By.ID, 'password')
user_submit = driver.find_element(By.ID, 'submit')


user_username.send_keys("student")
user_password.send_keys("Password123")
user_submit.click()
time.sleep(100)

# dumping the cookies / saving
pickle.dump(driver.get_cookies(). open("cookies.pkl","wb"))
driver.close()