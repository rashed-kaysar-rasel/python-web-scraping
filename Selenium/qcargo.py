from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()

driver.get("https://www.qrcargo.com/s/track-your-shipment?documentType=MAWB&documentPrefix=157&documentNumber=95819743")

driver.implicitly_wait(30)
track_details_elements =  driver.find_elements(By.XPATH, "//ul[contains(@class, 'qrds-cargo-track-details')]")


result_data = []

for index, track_element in enumerate(track_details_elements):
    title = track_element.find_element(By.XPATH, ".//li[2]/ul/li[1]").text
    total_item_and_weight_text = track_element.find_element(By.XPATH, ".//li[2]/ul/li[2]").text
    date = track_element.find_element(By.XPATH, ".//li[3]").text

    # Split the text on "|" and trim whitespace
    total_item, weight = map(str.strip, total_item_and_weight_text.split('|')[:2])

    result_data.append({
        'title': title,
        'total_item': total_item,
        'weight': weight,
        'date': date
    })

# Print or use the JSON data as needed
print(json.dumps(result_data, indent=4))
driver.quit()