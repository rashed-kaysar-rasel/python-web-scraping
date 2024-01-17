from bs4 import BeautifulSoup
import requests

website = "https://www.qrcargo.com/s/track-your-shipment?documentType=MAWB&documentPrefix=157&documentNumber=95819743"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content,"lxml")

print(soup.find('h2').get_text())
