
import urllib.request
from bs4 import BeautifulSoup


url = 'https://www.zhihu.com/question/64885015/answer/225276182' 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'   
headers = { 'User-Agent' : user_agent }   
request=urllib.request.Request(url,headers=headers)

response =urllib.request.urlopen(request)
str1= response.read()

soup = BeautifulSoup(str1,"html.parser")
list= soup.find_all(attrs={"class":"origin_image"})
print(len(list))
i=int(0)
for img in list:
    
    if 'lazy' in img.attrs['class']:
        continue
    jpgaddr= img.attrs['data-original']
    
    print(str(i)+" =  "+jpgaddr)
    request=urllib.request.Request(jpgaddr,headers=headers)
    response =urllib.request.urlopen(request)
    jpgdata= response.read() 
    picpath=r"d:\pythondata\bug1\pics\\"
    wholepath=picpath+str(i)+".jpg"
    jpgfile= open(wholepath,"wb")
    jpgfile.write(jpgdata)
    i+=1
    
htmlfile= open("d:\html.html","w")
print(str,file=htmlfile)
htmlfile.close()



#import urllib.parse
#import urllib.request
#url = 'http://www.baidu.com/'

#response = urllib.request.urlopen(url)
#the_page = response.read()
#print(the_page.decode('UTF8'))
