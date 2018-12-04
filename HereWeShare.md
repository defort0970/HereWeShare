#HereWeShare完成注意事項

## 編寫時出現警告

警告：SettingWithCopyWarning:  A value is trying to be set on a copy of a slice from a DataFrame

原因：df[] 再製作另一個 df_recorder[]，多此一舉，直接沿用就不會有問題。


## 好用的排序

插入最後一行，然後用排序方式，調整順序。

>df.loc[-1] = [.......]  # adding a row

>df.index = df.index + 1  # shifting index

>df = df.sort_index() 


## 針對資料中某行資料條件篩選

>df = df[df['某行'] == 判斷條件] 

可將符合判斷條件的資料留下！


## 針對資料中某行資料，也可善用 lambda 單行程式做 if 判斷

經由判斷條件，確認資料改為 A 或者為 B。

>df['某行'].apply(lambda x: 'A' if x == "判斷條件" else 'B')

