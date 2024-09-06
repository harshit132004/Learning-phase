from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options without headless mode for debugging
options = Options()
# options.add_argument("--headless")  # Comment this out to see the browser window
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")

# Set up the Chrome WebDriver
s = Service('C:/Users/LENOVO/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

print("Opening browser...")
# Open the website
driver.get('https://www.smartprix.com/mobiles')
print("Browser opened")
time.sleep(2)

# Use WebDriverWait to wait for the element to be clickable
wait = WebDriverWait(driver, 20)

# Scroll to bottom of page to ensure elements are loaded
print("Scrolling page...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # Allow time for elements to load after scrolling

# Try finding multiple elements using `find_elements`
print("Trying to find checkboxes...")
checkboxes = driver.find_elements(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label/input')
if len(checkboxes) > 0:
    print(f"Found {len(checkboxes)} checkboxes")
    checkboxes[0].click()  # Click the first checkbox
    time.sleep(1)
    checkboxes[1].click()  # Click the second checkbox
    print("Checkboxes clicked")
else:
    print("No checkboxes found")

# Close the driver after interaction
driver.quit()



