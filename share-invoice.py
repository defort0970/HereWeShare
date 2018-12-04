#!/usr/bin/env python3
# 此檔案乃做為學爾電子發票批次上傳的程式

import csv
import pandas as pd
import time
# import numpy as np

fpath="/Users/thomas/Downloads/"  
df = pd.read_csv(fpath+'智付通學爾開立發票 - 發票資料填寫.csv')
timestr = time.strftime("%Y%m%d")
txtp = fpath+'32355489_'+timestr+'.txt'

df['S']="S"

df['EmptyValue']="" #填空白用
df['載具類別']="2" #智付通為 2
df['稅別']="1"	# 1=應稅2=零稅率 3=免稅
df['稅率']="5"	# 稅別為應稅時，一般稅率請帶 5
df['未稅金額']=df['發票金額']/1.05
df['未稅金額']=df['未稅金額'].astype(float).round().astype(int)
df['稅金']=df['發票金額']-df['未稅金額']
df['明細錄別']="I"
df['商品單位']="式"
df['買受人統編']=df['買受人統編'].astype(str)
df['買受人統編']=df['買受人統編'].str.replace('nan', '')
df['買受人統編']=df['買受人統編'].apply(lambda x: x[0:8])
df['BorC']=df['買受人統編'].apply(lambda x: 'B2C' if x == "" else 'B2B')
df['索取紙本發票']=df['BorC'].apply(lambda x: 'N' if x == "B2C" else 'Y')
df['有無統編']=df['買受人統編'].apply(lambda x: 'N' if x == "" else 'Y')
df['商品數量']="1"
df['商品單價']=df['發票金額']
df['商品小計']=df['商品單價']

today = timestr[0:4]+'-'+timestr[4:6]+'-'+timestr[6:8]
df = df[df['日期'] == today] #偵測資料日否為今日，是的話，則留下資料

df = df[['S','自訂編號','BorC','買受人統編','買受人名稱（企業抬頭）','買受人email','買受人地址','載具類別','自訂編號','愛心碼','索取紙本發票','稅別','稅率','未稅金額','稅金','發票金額','發票品項','明細錄別','自訂編號','發票品項','商品數量','商品單位','商品單價','商品小計']] # rearrange column here
df.columns = ['S','自訂編號','BorC','買受人統編','買受人名稱（企業抬頭）','買受人email','買受人地址','2','自訂編號','EmptyValue','有無統編','稅別','稅率','未稅金額','稅金','發票金額','發票品項','I','自訂編號','發票品項','1','式','發票金額','發票金額']
df.loc[-1] = ['H','INVO','C0719718068','32355489',timestr,"","","","","","","","","","","","","","","","","","",""]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index() 

df.to_csv(txtp, header=None, index=False) #清除資料
content = open(txtp,'r', encoding='UTF-8')
contentata = content.read()
rep1=",,,,,,,,,,,,,,,,,,,"
rep2=",I,"
contentata = contentata.replace(rep1,"") 
contentata = contentata.replace(rep2,"\nI,") 
contentata = contentata[:-1]
content.close()

f = open(txtp,'w')
f.write(contentata)
f.close()