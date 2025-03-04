import requests
from bs4 import BeautifulSoup as bs   # for scrapping
from urllib.request import urlopen as uReq  # For making request to website 


# base URL
flipkart_url="https://www.flipkart.com"

# Make a request now
uClient=uReq(flipkart_url)

# Read HTML received
data=uClient.read()
# print(data)


# Search string 
search_string="iphone11"
#complete url with search string 
flipkart_url="https://www.flipkart.com/search?q="+search_string


# make a request

uClient=uReq(flipkart_url)
flipkart_page=uClient.read()

# as the page above is messey so we need to fix it or parse it 


flipkart_html=bs(flipkart_page,"html.parser")
print(flipkart_html)


