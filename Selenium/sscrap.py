from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.qrcargo.com/s/track-your-shipment?documentType=MAWB&documentPrefix=157&documentNumber=95819743")

driver.implicitly_wait(30)
# title = driver.find_element(By.CSS_SELECTOR, "h1")
# title = driver.find_element(By.CLASS_NAME, "sub-titletxt")

# wait = WebDriverWait(driver, 30)
# title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sub-titletxt")))
# title = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'sub-titletxt')]")))
title =  driver.find_element(By.XPATH, "//h2[contains(@class, 'sub-titletxt')]")


print(title.text)
driver.quit()