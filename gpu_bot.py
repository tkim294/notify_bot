import time
import os
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

ua = UserAgent();

driverLocation = './chromedriver'

opts = Options()
opts.add_argument("user-agent="+ua.random)
driver = webdriver.Chrome(driverLocation, options=opts)

while True:
    driver.get('https://www.bestbuy.com/site/playstation-5/ps5-consoles/pcmcat1587395025973.c?id=pcmcat1587395025973')
    # driver.get('https://www.bestbuy.com/site/nintendo-switch/nintendo-switch-consoles/pcmcat1484077694025.c?id=pcmcat1484077694025')

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    item_in_store = soup.find_all("button", {"class": "add-to-cart-button"})

    in_stock = []

    for product in item_in_store:
        if("Add" in product.text):
            item_tag = product.find_parent("li")
            in_stock.append(item_tag.find("a")['href'])

    base_url = "https://www.bestbuy.com"

    for url in in_stock:
        url = base_url + url
        os.system("osascript -e 'display notification \"BestBuy has ps5 in stock!\"\'")
        print(url)

    time.sleep(8)

    print("RUN FINISHED")