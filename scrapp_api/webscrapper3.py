# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:49:03 2019

@author: Malinda
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

class webscrapp:
    def scrapp(self,url):
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        para = soup.find('div',{'id':'paragraph'}).get_text()
        content = ''
    
        for p in soup.find_all('p'):    
            content = content+p.text
        
        
        para = "".join(line.strip() for line in para.split("\n"))
       
        return para
    
        #url = 'http://127.0.0.1:5000/summarize'
        #headers = {'Content-Type':'application/json'}
        #data = {'text':para}
    
        #response = requests.post(url=url,json=data,headers=headers)
        #return respon
        #print(response.text)
  
##take the following url as the example
##and i ve hosted the dummy site in htdocs
        
#x = 'http://127.0.0.1/Dummy/site1/grade11/topic2.html'
#g = webscrapp()
#r = g.scrapp(x) 


