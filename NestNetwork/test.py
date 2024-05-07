from bs4 import BeautifulSoup
import requests
url='https://codeforces.com/'
page=requests.get(url)

soup= BeautifulSoup(page.text, 'html')
print(soup)
 