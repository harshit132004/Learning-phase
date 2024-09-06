

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service("C:/Users/LENOVO/Desktop/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://google.com/")
time.sleep(3)

#fetch the search input box
user_input=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
user_input.send_keys("Jc bose university")
time.sleep(2)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link=driver.find_element(by=By.XPATH,value=' //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(4)

link_2=driver.find_element(by=By.XPATH,value='//*[@id="block-cmf-content-header-region-block"]/div/div/a[1]')
link_2.click()
time.sleep(4)

user_input_1=driver.find_element(by=By.XPATH,value='//*[@id="txtUserName"]')
user_input_1.send_keys("22001013052")
time.sleep(1)

user_input_1.send_keys(Keys.ENTER)
time.sleep(1)

user_input_2=driver.find_element(by=By.XPATH,value='//*[@id="txtPassword"]' )
user_input_2.send_keys("Harshit@123")
time.sleep(1)

user_input_2.send_keys(Keys.ENTER)
time.sleep(1)

link=driver.find_element(by=By.XPATH,value='//*[@id="btnSubmit"]')
link.click()
time.sleep(2)

user_input_1.send_keys(Keys.ENTER)
time.sleep(1)