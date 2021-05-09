import requests
from bs4 import BeautifulSoup
import pandas as pd
import pathlib as pl 
import numpy as np
import re


def get_price(url_core):
    url='https://www.fidelity.co.uk/factsheet-data/factsheet/'+url_core+'/key-statistics'
    print('parsing',url)
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find(class_='detail_value')
    
    for r in res:
        r=r.replace(',', '')
        if (r[-1]=='p'):
            prc=float(r[:-1])/100
        else:
            prc=float(r[1:])
    return prc  

p = pl.Path('C:\\')
f = p / 'Users' / 'simon' / 'Dropbox' /  'fidelity_info.csv'
df=pd.read_csv(f)
df['price'] = df['url-core'].apply(get_price)
f = p / 'Users' / 'simon' / 'Dropbox' /  'fidelity_prices.csv'
df.to_csv(f)
df

