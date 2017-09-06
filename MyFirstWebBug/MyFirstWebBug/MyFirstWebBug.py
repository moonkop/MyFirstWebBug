import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'
response =urllib.request.urlopen(url)
str= response.read()
soup = BeautifulSoup(str,"html.parser")
print(soup.find('html'))





#import urllib.parse
#import urllib.request
#url = 'http://www.baidu.com/'

#response = urllib.request.urlopen(url)
#the_page = response.read()
#print(the_page.decode('UTF8'))
