#!/usr/bin/python
# coding: UTF-8

import pandas as pd
from collections import defaultdict
from collections import Counter
import re
import numpy as np
import unicodedata
import codecs

#入力データ
file_dir = "./Data/"
file_name = "apple_support_NFKC"
file_type = ".txt"
input_docs_f = open(file_dir + file_name + file_type)

#1行読み込み
extract_text = input_docs_f.readline() 
#UTF-8に復号化
extract_text = extract_text.decode('utf-8', "ignore")
#Unicode正規化
extract_text = unicodedata.normalize('NFKC', extract_text)

num = 0
#特徴量を抽出するドキュメント(Pandas Frame)分、繰り返す
while extract_text:
    
    print extract_text
    
    #1行読み込み
    extract_text = input_docs_f.readline() 
    #UTF-8に復号化
    extract_text = extract_text.decode('utf-8', "ignore")
    #Unicode正規化
    extract_text = unicodedata.normalize('NFKC', extract_text)
    num = num + 1
    
input_docs_f.close() 

print "処理完了"
