from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
# print(response.text)
soup = BeautifulSoup(response, 'html.parser')

links = [i.get('href') for i in soup.find_all('a', class_="StyledPropertyCardDataArea-anchor")]
prices = [re.sub("[+/mo 1bd]","", i.text) for i in soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine")]
print(prices)


# https://docs.google.com/forms/d/e/1FAIpQLSeb87optrzogoT11OxsFNh5K5WrVZzV_rrvUreKxQrcCHZCxg/viewform?usp=header
