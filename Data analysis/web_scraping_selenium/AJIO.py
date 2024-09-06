from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service("C:/Users/LENOVO/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.ajio.com/s/gold-and-diamond-jewellery-4469-70481")
time.sleep(2)

old_height=driver.execute_script('return document.body.scrollHeight')

counter=1
while True:
  driver.execute_script('window.scrollTo(0 , document.body.scrollHeight)')
  time.sleep(2)
  new_height = driver.execute_script('return document.body.scrollHeight')

  print(counter)
  counter = counter + 1
  print(new_height)
  print(old_height)

  if new_height==old_height:
      break
  old_height=new_height

html = driver.page_source
with open('AJIO.html','w',encoding='utf-8') as f:
    f.write(html)


