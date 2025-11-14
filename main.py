import undetected_chromedriver as uc
from selenium.common import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import *
import time

if __name__ == "__main__":
    try:
        import certifi, os
        os.environ.setdefault("SSL_CERT_FILE", certifi.where())
        os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
    except Exception:
        pass

    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options)

    driver.get("https://www.oddschecker.com")

    wait = WebDriverWait(driver, 20)

    el = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept all']")))
    el.click()

    el = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log In']")))
    el.click()

    email = "jaaf2006@icloud.com"

    def log_in (email1, password1):
        log_in_email = wait.until(EC.element_to_be_clickable((By.ID, "loginUsername")))
        log_in_email.send_keys(email1)

        log_in_password = wait.until(EC.element_to_be_clickable((By.ID, "loginPassword")))
        log_in_password.send_keys(password1 + Keys.ENTER)

    log_in(email, password)

    try:
        while True:
            time.sleep(1)
            _ = driver.title
    except WebDriverException:
        pass
    finally:
        driver.quit()