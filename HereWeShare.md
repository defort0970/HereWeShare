#HereWeShare完成注意事項

## 編寫時出現警告

警告：SettingWithCopyWarning:  A value is trying to be set on a copy of a slice from a DataFrame

原因：df[] 再製作另一個 df_recorder[]，多此一舉，直接研究就不會有問題。




