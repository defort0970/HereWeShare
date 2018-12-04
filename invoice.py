#!/usr/bin/env python3
# 此檔案乃做為學爾電子發票批次上傳的程式

import csv
import pandas as pd
import time

fpath="/Users/thomas/Downloads/"  
df = pd.read_csv(fpath+'智付通學爾開立發票 - CSV下載.csv')
timestr = time.strftime("%Y%m%d")
txtp = fpath+'32355489_'+timestr+'.txt'

df.to_csv(txtp, index=False)
content = open(txtp,'r', encoding='UTF-8')
contentata = content.read()
rep1=",Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20,Unnamed: 21,Unnamed: 22,Unnamed: 23"
rep2=",I,"
contentata = contentata.replace(rep1,"") 
contentata = contentata.replace(rep2,"\nI,") 
contentata = contentata[:-1]
print(contentata)
content.close()

f = open(txtp,'w')
f.write(contentata)
f.close()