from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chromedriver = '.\chromedriver.exe'  

browser = webdriver.Chrome(chromedriver)
browser.get('http://hostellogin.srmuniv.ac.in/srmclb/')  # enter website

#unit test for chromedriver
url1 = browser.current_url
url2 = url1

while url1 == url2:
    username = browser.find_element_by_name('accountname')
    username.send_keys(os.environ.get("Email_ID"))  # enter username

    username = browser.find_element_by_name('password')
    username.send_keys(os.environ.get("Password"))  # enter password

    browser.execute_script("loginform()")
    url2 = browser.current_url
