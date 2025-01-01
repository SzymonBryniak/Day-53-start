from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
# print(response.text)
soup = BeautifulSoup(response, 'html.parser')

for i in soup.find_all('li', class_="ListItem-c11n-8-84-3-StyledListCardWrapper"):
  # print(i)2
  print(soup.find('a', class_="StyledPropertyCardDataArea-anchor"))
# https://docs.google.com/forms/d/e/1FAIpQLSeb87optrzogoT11OxsFNh5K5WrVZzV_rrvUreKxQrcCHZCxg/viewform?usp=header