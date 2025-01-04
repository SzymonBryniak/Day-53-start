from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
# print(response.text)
soup = BeautifulSoup(response, 'html.parser')

links = [i.get('href') for i in soup.find_all('a', class_="StyledPropertyCardDataArea-anchor")]
prices = [re.sub("[+/mo 1bd]","", i.text) for i in soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine")]
address = [i.text.strip() for i in soup.find_all('address')]

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
service = Service("C:\webdrivers\msedgedriver.exe")
driver = webdriver.Edge(options=edge_options, service=service)
driver.implicitly_wait(2)

def send_input(address, prices, link):
  time.sleep(1)
  address_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(address)
  
  price_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(prices)
  # https://docs.google.com/forms/d/e/1FAIpQLSeb87optrzogoT11OxsFNh5K5WrVZzV_rrvUreKxQrcCHZCxg/viewform?usp=header
  link_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(link)
  time.sleep(1)
  submit = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div").click()
  
for i in range(len(links)):
  driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeb87optrzogoT11OxsFNh5K5WrVZzV_rrvUreKxQrcCHZCxg/viewform?usp=header")
  send_input(address=address[i], prices=prices[i], link=links[i])
  
