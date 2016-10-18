
# coding: utf-8

# ### get csv from SIX page for indices and funds (ETFs)

# In[1]:

import urllib.request as request
import time
import requests
from urllib.parse import urlencode
from pprint import pprint

# url_for_indices = 'https://www.six-swiss-exchange.com/indices/info_market_data_download.csv'
# url_for_funds = 'https://www.six-swiss-exchange.com/funds/info_market_data_download.csv'

fundliste = {'SPI TR' : ('SPI', 'indices', 'CH0009987501CHF9'),
            'iShares Core SPI (CH) CHSPI' : ('CHSPI', 'funds', 'CH0237935652CHF4'),
            'UBS ETF SPI (CHF) A SPICHA' : ('SPICHA', 'funds', 'CH0131872431CHF4'),
            }
kursTyps = {'itd' : '0', # intraday Values
          'hst' : '107'} # historical daily Values (five month)


codelist = []
'''
prepare list with all needed codes
    name = Valorensymbol
    urlcode = different url for 'funds' or 'indices'
    identifier = code for specific item with ISIN
    kurstyp = 0 for intraday and 107 for historical values
    domain = domain code to be passed as data
'''# prepare list with all needed codes
for name, urlcode, identifier in fundliste.values():
    #print(name, urlcode, identifier)
    for kurstyp, domain in kursTyps.items():
        fname = 'SIXcsv/SX'+kurstyp+'_'+name+'_'+time.strftime('%Y-%m-%d_%H%M%S')+'.csv'
        url = 'https://www.six-swiss-exchange.com/'+urlcode+'/info_market_data_download.csv'
        codelist.append((fname,identifier, domain, url))


for fname, ident, domain, url in codelist:
    data = urlencode({'id' : ident, 'domain' : domain, 
                      'actionSUBMIT.x' : '10', 'actionSUBMIT.y' : '11'}).encode('ascii')
    # save downloaded data as fname.csv
    fname, headers = request.urlretrieve(url, filename=fname, data=data)
    print(fname, headers['Content-Type']) # correct Content-Type is 'text/csv'
    


# In[ ]:



