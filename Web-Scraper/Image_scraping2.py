# Importing module urllib and BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Reading URL with urlopen()
data = urlopen('https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/')

# Passing the requests into a BeautifulSoup() function
soup = BeautifulSoup(data, 'html.parser')

# Using 'img' tag to find them all tag ('src')
images = soup.find_all('img')
 
for item in images:
    print(item['src'])
