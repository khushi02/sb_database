from requests import get
from bs4 import BeautifulSoup
import pandas as pd

names = []
amounts = []

url = 'https://supportlocal.usatoday.com/cities/'
response = get(url)
#print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')
#print(type(html_soup))

city_containers = soup.find_all('a', class_ = 'sl-cities-list-item')
#print(type(city_containers))
print(len(city_containers))

city_name = soup.find('a', class_ = 'sl-cities-list-item').h4.text
print(city_name)

num_sb = soup.find('div', class_ = 'sl-cities-list-item-count').span.text
print(num_sb)

for container in city_containers:
    name = container.find('h4').text
    names.append(name)
    
    num = container.find('div', class_ = 'sl-cities-list-item-count').span.text
    amounts.append(num)
    
test_df = pd.DataFrame({'City Name': names,
                        'Number of SBs': amounts})

print(test_df)