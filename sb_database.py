from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# Declaring lists to store data
cities = []
sbs = []
names = []
addresses = []
images = []

# Access city names and number of SBs
url = 'https://supportlocal.usatoday.com/cities/'
response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

city_containers = soup.find_all('a', class_ = 'sl-cities-list-item')

for container in city_containers:
    city = container.find('h4').text
    cities.append(city)
    
    num = container.find('div', class_ = 'sl-cities-list-item-count').span.text
    sbs.append(num)
    
city_df = pd.DataFrame({'City Name': cities,
                        'Number of SBs': sbs})

print(city_df)

# Access individual city info
for city in cities:
    url_name = city.replace(' ', '-')
    url_name = url_name.replace(',', '')
    url_name = url_name.lower()
    city_url = 'https://supportlocal.usatoday.com/city/' + url_name
    city_response = get(city_url)
    
    city_soup = BeautifulSoup(city_response.text, 'html.parser')
    sb_containers = city_soup.find_all('div', class_ = 'sl-business-list-item')
    
    for container in sb_containers:
        name = container.find('div', class_= 'sl-business-list-item-details').p.a.text
        names.append(name)
        
        address = container.find('p', class_ = 'address')
        addresses.append(address)
        
        image = container.find('div', class_ = 'sl-business-list-item-img')