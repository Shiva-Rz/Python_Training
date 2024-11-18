''' Use the BeautifulSoup and requests Python packages to print out a list of all the article titles 
    on the New York Times tech page (https://www.nytimes.com/section/opinion/technology)'''

import requests
from bs4 import BeautifulSoup

url = 'https://relevantz.com'
html = requests.get(url)
data = BeautifulSoup(html.text, 'html.parser')
print(data.header.text)