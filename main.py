from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path = "/Users/jaafarmohammed/Desktop/arbi/chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://www.bet365.com/#/HO/")

time.sleep(10)

driver.quit()