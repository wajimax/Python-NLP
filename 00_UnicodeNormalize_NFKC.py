#!/usr/bin/python
# coding: UTF-8

import pandas as pd
from collections import defaultdict
from collections import Counter
import re
import numpy as np
import unicodedata
import codecs

#入力データ（UTF-8）のリスト
file_dir = "./Data/"
file_name_list = ["apple_support"]
file_type = ".txt"

#出力データセット
file_type = ".txt"
out_dir = "./Data/"

print "ファイル読み込み完了"

#入力データごとに繰り返す
for file_name in file_name_list:
    open_file_name = file_dir + file_name + file_type
    open_file = open(open_file_name,"r")
    
    #1行を文字列として読み込む(改行文字も含まれる)
    extract_text = open_file.readline() 
    #UTF-8に復号化、欠損値除去
    extract_text = extract_text.decode('utf-8', "ignore")
    #Unicode正規化
    extract_text = unicodedata.normalize('NFKC', extract_text)
    
    #出力ファイル
    output_file = open(out_dir + file_name + "_NFKC" + file_type , 'w')
    
    while extract_text:       
        #ファイル出力
        output_file.write(extract_text.encode('utf-8'))
        
        #1行を文字列として読み込む(改行文字も含まれる)
        extract_text = open_file.readline() 
        
        #UTF-8に復号化、欠損値除去
        extract_text = extract_text.decode('utf-8', "ignore")
        
        #Unicode正規化
        extract_text = unicodedata.normalize('NFKC', extract_text)

    #出力ファイルをクローズ
    output_file.close()

print "出力データ作成完了"
