from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s=Service('C:/Users/LENOVO/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input"]').click()
time.sleep(2)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(4)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
time.sleep(5)