import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

listings_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(listings_url, headers=my_headers)

soup = BeautifulSoup(response.text, "html.parser")

rental_listings_links = []
rental_prices_listings = []
rental_listings_addresses = []

links = soup.find_all(name="a", class_="list-card-link")
prices = soup.find_all(class_="list-card-price")
addresses = soup.find_all(class_="list-card-addr")

for link in links:
    if link['href'].startswith('/b'):
        link['href'] = 'https://zillow.com' + link['href']
        rental_listings_links.append(link['href'])
    else:
        rental_listings_links.append(link.get("href"))

rental_listings_links = list(dict.fromkeys(rental_listings_links))

for price in prices:
    price_text = price.getText()
    strip_price = price_text.strip("/mo+ 1 bd")
    rental_prices_listings.append(strip_price)

for address in addresses:
    address_text = address.getText()
    clean_address = address_text.replace("|", "")
    rental_listings_addresses.append(clean_address)

print(f"Total Number of address listings: {len(rental_listings_addresses)}")
print(f"Total number of price listings: {len(rental_prices_listings)}")
print(f"Total number of link listings: {len(rental_listings_links)}")

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd-v61M7-rn_HfNEfVhbjuFkoPHXpBrSPw2263-PHn08S2NPA/viewform?usp=sf_link")

# for i in range(len(rental_listings_addresses)):
for i in range(len(rental_listings_addresses)):
    time.sleep(1)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(rental_listings_addresses[i])
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(rental_prices_listings[i])
    property_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(rental_listings_links[i])
    sbt_btn = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    sbt_btn.click()
    if i != len(rental_listings_addresses):
        sbt_another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        sbt_another_response.click()
        
    

