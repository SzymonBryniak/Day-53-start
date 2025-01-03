from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
# print(response.text)
soup = BeautifulSoup(response, 'html.parser')

links = [i.get('href') for i in soup.find_all('a', class_="StyledPropertyCardDataArea-anchor")]
prices = [re.sub("[+/mo 1bd]","", i.text) for i in soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine")]
address = [re.sub("[\n]","", i.text) for i in soup.find_all('address')]

print(address)
