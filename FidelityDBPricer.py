import sys
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from pathlib import Path
import requests
from bs4 import BeautifulSoup
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

# https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql 
# dialect+driver://username:password@host:port/database'
from sqlalchemy.types import Integer, Text, String, DateTime, VARCHAR, Float
sqlEngine=create_engine('mysql+pymysql://guest:guest@127.0.0.1/finance', pool_recycle=3600,echo=True)
dbConnection=sqlEngine.connect()
df=pd.read_sql("select * from fidelity_info", dbConnection)
df['price'] = df['urlcore'].apply(get_price)
df.to_sql(
    'fidelity_latest_prices',
    sqlEngine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={
        "urlcore": VARCHAR(100),
        "fundlabel": VARCHAR(50),
        "price" : Float
    }
)