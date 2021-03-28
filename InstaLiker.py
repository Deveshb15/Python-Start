from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://instagram.com")

username = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('readaftercomplete')

password = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pswd = getpass()
password.send_keys(pswd)

login_btn = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login_btn.click()
time.sleep(5)

search_box = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_box.send_keys('elite_netfllix')
time.sleep(3)

search_box.send_keys(Keys.ENTER)
search_box.send_keys(Keys.ENTER)


post = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')
post.click()
like_btn = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like_btn.click()
next_btn = chrome.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
next_btn.click()