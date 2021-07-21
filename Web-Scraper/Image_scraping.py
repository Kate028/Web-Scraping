## install python libraries from terminal for pulling data out of HTML files.
# pip install bs4
# pip install requests


# step 1: import modules
# step 2: make requests instance and pass into URL
# step 3: Pass the requests into a BeautifulSoup() function
# step 4: Use 'img' tag to find them all tag ('src')
import requests
from bs4 import BeautifulSoup

def image_scraping(url):
    r = requests.get(url)
    return r.text

data = image_scraping("https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/")
soup = BeautifulSoup(data, 'html.parser')
for item in soup.find_all('img'):
    print(item['src']) 
