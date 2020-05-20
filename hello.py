import requests        #导入requests包   爬取网页上的内容
import re
from bs4 import BeautifulSoup
url='http://www.cntour.cn/'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
print(result)