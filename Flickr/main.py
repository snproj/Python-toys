import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from init_driver import driver

driver.get("https://identity.flickr.com")

email = "dragonzhengyew@gmail.com"
password = "Schoolcorps9905"

email_login = driver.find_elements_by_tag_name("input")[0]

email_login.send_keys(Keys.BACKSPACE)
email_login.send_keys(email)
email_login.send_keys(Keys.RETURN)

time.sleep(3)

password_login = driver.find_elements_by_tag_name("input")[1]

password_login.send_keys(Keys.BACKSPACE)
password_login.send_keys(password)
password_login.send_keys(Keys.RETURN)

time.sleep(1)

driver.get("https://www.flickr.com/photos/141372003@N05/")