import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


# <h3 class="detail_value text-grey-800 mb-8 no-wrap">
#            £0.8139
#     </h3>

ticks=['GB00B2PLJN71-artemis-high-income-fund-class-i-inc',
       'GB00B5LXGG05-axa-framlington-american-growth-z-acc',
       'GB00B4W52V57-axa-framlington-global-technology-z-acc',
       'GB00B8K6W529-bny-mellon-long-term-glob-eq-inst-w-acc',
       'GB00BD1RHT82-fif---fidelity-cash-fund-w-accumulation',
       'GB00BFRT3504-fidelity-european-w-acc-(uk',
       'LU1033664027-fid-funds-latin-america-fund-w-acc-gbp',
       'GB00B8HT7153-fidelity-global-special-situations-w-acc',
       'GB0033874321-fssa-greater-china-growth-b-acc',
       'GB00B80QFR50-hsbc-ftse-100-index-acc-c',
       'GB00B3FJQ482-jpm-us-equity-income-fund-c---net-acc',
       'GB00B4T6SD53-jupiter-strategic-bond-i-class-acc',
       'GB00B544HM32-jupiter-strategic-bond-i-class-inc',
       'GB00B0CNGM05-legal--general-uk-index-trust-i-inc',
       'GB00B18B9X76-lf-lindsell-train-uk-equity-fund-acc',
       'GB00B1YBRL59-mg-corporate-bond-fund-i-acc',
       'GB0033874768-stewart-investors-asia-pac-lead-sus-b-ac',
       'GB00B1FXTG93-stewart-invstrs-indian-subcont-sust-b-ac',
       'JE00B1VS3770-wisdomtree-metal-securities']
for tick in ticks:
    url='https://www.fidelity.co.uk/factsheet-data/factsheet/'+tick+'/key-statistics'
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    res = soup.find(class_='detail_value')
    
    for r in res:
        r=r.replace(',', '')
        if (r[-1]=='p'):
            prc=float(r[:-1])/100
        else:
            prc=float(r[1:])
        print (tick[13:],prc)
   