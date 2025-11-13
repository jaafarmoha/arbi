from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



service = Service(executable_path = "/Users/jaafarmohammed/Desktop/arbi/chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://www.oddschecker.com")

wait = WebDriverWait(driver, 20)

el = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept all']")))
el.click()
el = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log In']")))
el.click()

try:
    while True:
        time.sleep(1)
        _ = driver.title  
except WebDriverException:
    pass
finally:
    driver.quit()