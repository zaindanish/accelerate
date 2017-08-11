import requests;
from bs4 import BeautifulSoup


f=open('data.txt','w');

def techSinaCrawler():
    url="http://tech.sina.com.cn/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for li in soup.findAll('li',{'data-sudaclick': 'yaowenlist-1'}):
        #f.write(li.prettify());
        for link in li.findAll('a'):
            href = link.get('href')
            
            #  got the links 
            techSinaInsideLinkCrawler(href);
            
            
def techSinaInsideLinkCrawler(url):

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for data in soup.findAll('h1',{'id': 'main_title'}):

        f.write(data.prettify());
        
techSinaCrawler();