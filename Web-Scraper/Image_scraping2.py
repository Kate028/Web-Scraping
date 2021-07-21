# Using urllib and BeautifulSoup
# Import module
# read URL with urlopen()
# Pass the requests into a BeautifulSoup() function
# Use 'img' tag to find them all tag ('src')



from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/')
soup = BeautifulSoup(data, 'html.parser')
images = soup.find_all('img')
 
for item in images:
    print(item['src'])
