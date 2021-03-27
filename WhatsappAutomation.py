from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)

chrome.get("https://web.whatsapp.com")
time.sleep(7)

search_box = chrome.find_element_by_class_name("_2_1wd")
search_box.send_keys("Jeet")
search_box.send_keys(Keys.ENTER)

for i in range(0,100):
    type_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    type_box.send_keys("100 automated messages under 10 sec")
    type_box.send_keys(Keys.ENTER)