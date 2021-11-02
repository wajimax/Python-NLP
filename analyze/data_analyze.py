# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
import mecab_lib
from collections import defaultdict

#指定したファイルを形態素解析
def analyze_data(_fileName):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#設定ファイルから解析対象の品詞を読み込み
	ja_pos = ["名詞","動詞","形容詞","副詞"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#形態素解析のファイルを保存するファイルパス
	ja_file_wakachi = open(_fileName + "_wakachi","w")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.text_ja(ja_line,ja_pos,ja_form)
		
		ja_file_wakachi.writelines("\t".join(ja_line_tokens) + "\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
	
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_wakachi.close()

#指定したファイルを形態素解析
def analyze_sentiment(_fileName,_sentiment_dic):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#設定ファイルから解析対象の品詞を読み込み
	ja_pos = ["名詞","動詞","形容詞","副詞"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#評価極性計算結果を保存するファイルパス
	ja_file_sentiment = open(_fileName + "_sentiment","w")
	
	#返却値用の配列
	ja_list = []
	
	#評価極性ファイルをオープン
	sentiment_dic = open(_sentiment_dic)
	
	#評価極性リスト
	sentiment_dic_list = defaultdict(lambda:0) 
	
	#評価極性辞書を読み込み
	for sentiment_dic_line in sentiment_dic:
		
		#文字列分割
		sentiment_dic_line_list = sentiment_dic_line.rstrip().split(":")
		
		#極性値を配列に格納
		sentiment_dic_list[sentiment_dic_line_list[0]] = sentiment_dic_line_list[1]
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#評価極性ファイルに書き込み
	ja_file_sentiment.writelines("ポジティブ単語頻度\tネガティブ単語頻度\tポジティブ単語比率\tネガティブ単語比率\t平均評価極性値\r\n")
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#単語数
		word_count = 0
		
		#ポジティブ単語の頻度と比率
		positive_count = 0
		positive_ratio = 0
		
		#ネガティブ単語の頻度と比率
		negative_count = 0
		negative_ratio = 0
		
		#合計値
		sum_value = 0
		
		#平均値
		average_value = 0
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.text_ja(ja_line,ja_pos,ja_form)
		
		#形態素ごとに繰り返す
		for ja_line_token in ja_line_tokens:
			
			#単語数に加算
			word_count += 1
			
			sentiment_value = sentiment_dic_list[ja_line_token]
			
			#辞書の値で分岐
			if float(sentiment_value) >= 0:
				#ポジティブに加算
				positive_count += 1
				
			elif float(sentiment_value) < 0:
				#ネガティブに加算
				negative_count += 1
				
			else:
				#ニュートラルに加算
				neutral_count += 1
			
			#合計値に加算
			sum_value = sum_value + float(sentiment_dic_list[ja_line_token])
		
		#平均値を算出
		if word_count > 0:
			average_value = sum_value / word_count
		else:
			average_value = 0
		
		#比率を算出
		if word_count > 0:
			positive_ratio = positive_count * 1.0 / word_count
			negative_ratio = negative_count * 1.0 / word_count
		
		#評価極性ファイルに書き込み
		ja_file_sentiment.writelines(str(positive_count) + "\t" + str(negative_count) + "\t" + str(positive_ratio) + "\t" + str(negative_ratio) + "\t" + str(average_value) + "\r\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
	
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_sentiment.close()

#指定したファイルの品詞情報を取得
def analyze_pos(_fileName):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#設定ファイルから解析対象の品詞を読み込み
	ja_pos = ["名詞","動詞","形容詞","副詞"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#形態素解析のファイルを保存するファイルパス
	ja_file_pos = open(_fileName + "_posdata","w")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ヘッダ
	ja_file_pos.writelines("名詞\t")
	ja_file_pos.writelines("動詞\t")
	ja_file_pos.writelines("形容詞\t")
	ja_file_pos.writelines("副詞\t")
	ja_file_pos.writelines("文字数\t")
	ja_file_pos.writelines("\r\n")
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.posTagger(ja_line,ja_pos)
		
		#品詞返却用の配列
		pos_count_list = count_pos(ja_line_tokens)
		
		#品詞数のカウント
		ja_file_pos.writelines(str(pos_count_list["名詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["動詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["形容詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["副詞"]) + "\t")
		
		#文字列長を書き込み
		ja_file_pos.writelines(str(len(ja_line)))
		
		#改行
		ja_file_pos.writelines("\r\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
		
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_pos.close()

#指定したファイルの品詞情報を取得
def analyze_pos_Type1all(_fileName):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#設定ファイルから解析対象の品詞を読み込み
	ja_pos = ["連体詞","接頭詞","名詞","動詞","形容詞","副詞","接続詞","助詞","助動詞","感動詞","記号","フィラー","その他","未知語"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#形態素解析のファイルを保存するファイルパス
	ja_file_pos = open(_fileName + "_pos_Type1all","w")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ヘッダ
	ja_file_pos.writelines("連体詞\t")
	ja_file_pos.writelines("接頭詞\t")
	ja_file_pos.writelines("名詞\t")
	ja_file_pos.writelines("動詞\t")
	ja_file_pos.writelines("形容詞\t")
	ja_file_pos.writelines("副詞\t")
	ja_file_pos.writelines("接続詞\t")
	ja_file_pos.writelines("助詞\t")
	ja_file_pos.writelines("助動詞\t")
	ja_file_pos.writelines("感動詞\t")
	ja_file_pos.writelines("記号\t")
	ja_file_pos.writelines("フィラー\t")
	ja_file_pos.writelines("その他\t")
	ja_file_pos.writelines("未知語")
	ja_file_pos.writelines("\r\n")
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.posTagger(ja_line,ja_pos)
		
		#品詞返却用の配列
		pos_count_list = count_pos(ja_line_tokens)
		
		#品詞数のカウント
		ja_file_pos.writelines(str(pos_count_list["連体詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["接頭詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["名詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["動詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["形容詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["副詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["接続詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["助詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["助動詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["感動詞"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["記号"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["フィラー"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["その他"]) + "\t")
		ja_file_pos.writelines(str(pos_count_list["未知語"]))
		#文字列長を書き込み
		ja_file_pos.writelines(str(len(ja_line)))
		
		#改行
		ja_file_pos.writelines("\r\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
		
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_pos.close()

#指定したファイルのSubtype情報を取得
def analyze_proper_noun(_fileName):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#解析対象のSubtype
	ja_subtype = ["一般","人名","組織","地域"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#形態素解析のファイルを保存するファイルパス
	ja_file_subtype = open(_fileName + "_proper_noun","w")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ヘッダ
	ja_file_subtype.writelines("一般\t")
	ja_file_subtype.writelines("人名\t")
	ja_file_subtype.writelines("組織\t")
	ja_file_subtype.writelines("地域")
	ja_file_subtype.writelines("\r\n")
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.subtypeTagger(ja_line,ja_subtype)
		
		#Subtype返却用の配列
		subtype_count_list = count_subtype(ja_line_tokens)
		
		#Subtype数のカウント
		ja_file_subtype.writelines(str(subtype_count_list[u"一般"]) + "\t")
		ja_file_subtype.writelines(str(subtype_count_list[u"人名"]) + "\t")
		ja_file_subtype.writelines(str(subtype_count_list[u"組織"]) + "\t")
		ja_file_subtype.writelines(str(subtype_count_list[u"地域"]))
		
		#改行
		ja_file_subtype.writelines("\r\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
		
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_subtype.close()

#指定したファイルのdetail1情報を取得
def analyze_detail1(_fileName):
	
	#ファイル名をオープン
	ja_file = open(_fileName)
	
	#解析対象のdetail1
	ja_subtype = ["形容動詞語幹"]
	
	#設定ファイルから活用形を読み込み
	ja_form = "basic"
	
	#形態素解析のファイルを保存するファイルパス
	ja_file_subtype = open(_fileName + "_detail1","w")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ヘッダ
	ja_file_subtype.writelines("形容動詞語幹")
	ja_file_subtype.writelines("\r\n")
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#対象行の形態素解析処理
		ja_line_tokens = mecab_lib.detail1Tagger(ja_line,ja_subtype)
		
		#Subtype返却用の配列
		subtype_count_list = count_subtype(ja_line_tokens)
		
		#Subtype数のカウント
		ja_file_subtype.writelines(str(subtype_count_list[u"形容動詞語幹"]))
		
		#改行
		ja_file_subtype.writelines("\r\n")
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
		
	#ファイルポインタをクローズ
	ja_file.close()
	ja_file_subtype.close()

#感情情報の集計用
def make_sentiment_jadic(_fileName,_dicfile):
	takamura_file = open(_dicfile,"r")
	takamura_dic = defaultdict(lambda:0)
	takamura_line = takamura_file.readline()
	
	while takamura_line:
		takamura_line = takamura_line.rstrip()
		takamura_line_list = takamura_line.split(":")
		#dic_key_kan = takamura_line_list[0] + ":" + takamura_line_list[2]
		#dic_key_hira = takamura_line_list[1] + ":" + takamura_line_list[2]
		dic_key_kan = takamura_line_list[0]
		dic_key_hira = takamura_line_list[1]


#品詞情報のカウント用処理
def count_pos(_pos_list):
	
	#品詞とカウントの辞書型
	pos_count_list = defaultdict(lambda:0) 
		
	for pos_tag in _pos_list:
		pos_count_list[pos_tag] += 1	
	return pos_count_list

#Subtypeのカウント用処理
def count_subtype(_subtype_list):
	
	#品詞とカウントの辞書型
	subtype_count_list = defaultdict(lambda:0) 
	for subtype_tag in _subtype_list:
		subtype_count_list[subtype_tag] += 1
	return subtype_count_list

