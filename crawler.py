import requests;
from bs4 import BeautifulSoup

f=open('data.txt','w');

def techSinaCrawler():
    url="http://tech.sina.com.cn/"
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    for li in soup.findAll('li',{'data-sudaclick': 'yaowenlist-1'}):
        for link in li.findAll('a'):
            href = link.get('href')
            techSinaInsideLinkCrawler(href);            
            
def techSinaInsideLinkCrawler(url):
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    for data in soup.findAll('h1',{'id': 'main_title'}):
        str='main_title'+':'+ data.string
        f.write(str);
        f.write('\n');
        
        
techSinaCrawler();