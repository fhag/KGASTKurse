
# coding: utf-8

# ### get daily xls from KGAST site - needs to be run every day

import urllib.request as request
import time

getxls = 'http://www.kgast.ch/dynasite.cfm?cmd=cprodukt_produkt_excel_export&skipfurl=1'

# get first link for today's xls
with request.urlopen(getxls) as response:
   getxlslink = response.read().decode()

#create filename
fname = 'KGASTxls/KGAST'+time.strftime('%Y-%m-%d--%H%M%S')+'.xls'

# save today's xls as fname
fname, headers = request.urlretrieve(getxlslink, filename=fname)
# show result and filename
print(headers, fname)



