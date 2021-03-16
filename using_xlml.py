# install packages using terminal
# pip install requests
# pip install lxml

# 1. Send a link and get the response from the sent link
# 2. Then convert response object to a byte string.
# 3. Pass the byte string to ‘fromstring’ method in html class in lxml module.
# 4. Get to a particular element by xpath.
# 5. Use the content according to your need.

from bs4 import BeautifulSoup
import requests

from lxml import html

# url of website from where we will be scraping date
url = 'https://www.geeksforgeeks.org/python-tools-world-web-scraping/?ref=rp'

# path to particular element we want to scrape
path = '//*[@id="main"]'

response = requests.get(url)
byte_data = response.content

# get filtered source code
source_code = html.fromstring(byte_data)

# jump to preferred html element
tree = source_code.xpath(path)

# print texts in first element in list
print(tree[0].text_content())
soup = BeautifulSoup(source_code)
print(soup.prettify())


# Urllib2 : Urllib2 is a python module used for fetching URL's. It offers a very simple interface, in the form of urlopen function, which is capable of fetching URL’s using different protocols like HTTP, FTP etc.
# Using urllib2 module 
         
# Requests : Requests does not come pre-installed with Python. Requests allows to send HTTP/1.1 requests. One can add headers, form data, multipart files and parameters with simple Python dictionaries and access the response data in the same way.
# Installing requests can be done using pip.         
# pip install requests

# BeautifulSoup : Beautiful soup is a parsing library that can use different parsers. Beautiful Soup’s default parser comes from Python’s standard library. It creates a parse tree that can be used to extract data from HTML; a toolkit for dissecting a document and extracting what you need. It automatically converts incoming documents to Unicode and outgoing documents to UTF-8.
# pip can be used to install BeautifulSoup 
# pip install beautifulsoup4

# Lxml : Lxml is a high-performance, production-quality HTML and XML parsing library. If the user need speed, then go for Lxml. Lxml has many modules and one of the module is etree , which is responsible for creating elements and structure using these elements.
# One can start using lxml by installing it as a python package using pip tool :

# pip install lxml

# Selenium : Some websites use javascript to serve content. For example, they might wait until you scroll down on the page or click a button before loading certain content. For these websites, selenium is needed. Selenium is a tool that automates browsers, also known as web-drivers. It also comes with Python bindings for controlling it right from your application.
# pip package is used to install selenium :

# pip install selenium
