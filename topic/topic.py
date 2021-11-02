# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import conf
import math
from collections import defaultdict

#gensimの辞書・コーパスの作成
def topic_corpus_maker(_fileName,_input_filepath,_output_filepath):
	
	#辞書の保存パス
	gensim_dic_path = _output_filepath + _fileName + "_gensimdic"
	
	#コーパスの保存パス
	gensim_corpa_path = _output_filepath + _fileName + "_gensimcorpa"
	
	filepath = _input_filepath + _fileName
	
	print filepath
	
	#ファイルの読み込み
	ja_file = open(filepath,"r")
	
	#返却値用の配列
	ja_list = []
	
	#1行目の読み込み
	ja_line = ja_file.readline()
	
	#ファイルの最終行まで繰り返す
	while ja_line:
		
		#TABで区切られているわかち書きのテキストを読み込み
		ja_line_tokens = ja_line.split("\t")
		
		#二次元配列に格納
		ja_list.append(ja_line_tokens)
		
		#ファイルポインタを次へ
		ja_line = ja_file.readline()
		
	#ファイルポインタをクローズ
	ja_file.close()
	
	#二次元配列を元にgensimの辞書を作成
	gensim_dic = gensim_lib.tokens_To_GensimDic(ja_list)
	
	#gensimの辞書をサーバに保存
	gensim_lib.store_The_GensimDic(gensim_dic,gensim_dic_path)
	
	#二次元配列を元にgensimのコーパスを作成
	gensim_corpa = gensim_lib.tokens_To_GensimCorpus(ja_list,gensim_dic)
	
	#gensimのコーパスを保存
	gensim_lib.store_The_GensimCorpus(gensim_corpa,gensim_corpa_path)
	

#LDAトピックの抽出
def lda_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path,_topic_num):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#LDAトピックを抽出
	lda_topic = gensim_lib.extraction_LdaTopic(gensim_dic,gensim_corpa,_topic_num)
	
	#LDAトピックを保存
	gensim_lib.store_The_LdaTopic(lda_topic,_topic_path)
	
	return lda_topic
	
#LSIトピックの抽出
def lsi_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path,_topic_num):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#TF-IDFのインスタンス作成
	gensim_tfidf_instance = gensim_lib.gensimCorpus_To_TfidfInstance(gensim_corpa)
	
	#TF-IDFのコーパスを作成
	gensim_tfidf_corpa = gensim_lib.gensimCorpus_To_TfidfCorpus(gensim_corpa,gensim_tfidf_instance)
	
	#LSIトピックを抽出
	lsi_topic = gensim_lib.extraction_LsiTopic(gensim_dic,gensim_tfidf_corpa,_topic_num)
	
	#LSIトピックを保存
	gensim_lib.store_The_LsiTopic(lsi_topic,_topic_path)
	
	return lsi_topic
	
#HDPトピックの出力
def hdp_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#HDPトピックを抽出
	hdp_topic = gensim_lib.extraction_HdpTopic(gensim_dic,gensim_corpa)
	
	#HDPトピックを保存
	gensim_lib.store_The_HdpTopic(hdp_topic,_topic_path)
	
	#抽出したHDPトピックの一部を抽出
	#hdp_topic_extract = hdp_topic.print_topics(topics=_topic_num, topn=10)
	hdp_topic_extract = hdp_topic.print_topics(topics=-1, topn=10)
	
	return hdp_topic_extract
	
#トピックテキストの保存
def topic_to_list(_topic):
	
	#単語分布と出現確率のリスト
	extraction_list = []
	word_list = []
	probability_list = []
	
	for topic in _topic.show_topics(-1):
		print topic
		#topic.strip()
		#topic_list = topic.split('+')
		#2018/10/13
		topic_str = topic[1].strip()
		topic_list = topic_str.split('+')
		topic_word_line = ""
		topic_probability_line = ""
		
		for topic_line in topic_list:
			topic_line.strip()
			topic_element = topic_line.split('*')
			topic_word_line = topic_word_line + topic_element[1]
			topic_probability_line = topic_probability_line + topic_element[0]
			
		word_list.append(topic_word_line)
		probability_list.append(topic_probability_line)
		
		extraction_list.append(word_list)
		extraction_list.append(probability_list)
	
	return extraction_list
	
#トピックテキストの保存(HDP)
def topic_to_list_hdp(_topic):
	
	#単語分布と出現確率のリスト
	extraction_list = []
	word_list = []
	probability_list = []
	
	for topic in _topic:
		print topic
		topic.strip()
		topic_list = topic.split('+')
		topic_word_line = ""
		topic_probability_line = ""
		
		for topic_line in topic_list:
			topic_line.strip()
			topic_element = topic_line.split('*')
			topic_word_line = topic_word_line + topic_element[1]
			topic_probability_line = topic_probability_line + topic_element[0]
			
		word_list.append(topic_word_line)
		probability_list.append(topic_probability_line)
		
		extraction_list.append(word_list)
		extraction_list.append(probability_list)
	
	return extraction_list

#LDAトピックの割当
def lda_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensimのトピックを読み込み(LDA)
	gensim_topic = gensim_lib.load_The_LdaTopic(_topic)
	
	#割当対象のファイル
	allot_file = open(_wakachi_path,"r")
	
	#返却用の変数
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#ファイルの最終行まで繰り返す
	while allot_file_line:
		
		#TABで区切られているわかち書きのテキストを読み込みしトークン化
		allot_file_line_tokens = allot_file_line.split()
		
		#トークン化された単語群をBOWに変換
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#トピックを割り当てトピックの確率分布を取得
		allot_topic = gensim_lib.doc_to_ldatopic_distribution(allot_file_line_bow,gensim_topic)
		
		#トピックを配列に追加
		allot_topic_list.append(allot_topic)
		
		#ファイルポインタを次へ
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#LSIトピックの割当
def lsi_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensimのトピックを読み込み(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic)
	
	#割当対象のファイル
	allot_file = open(_wakachi_path,"r")
	
	#返却用の変数
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#ファイルの最終行まで繰り返す
	while allot_file_line:
		
		#TABで区切られているわかち書きのテキストを読み込みしトークン化
		allot_file_line_tokens = allot_file_line.split()
		
		#トークン化された単語群をBOWに変換
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#トピックを割り当てトピックの確率分布を取得
		allot_topic = gensim_lib.doc_to_lsitopic_distribution(allot_file_line_bow,gensim_topic)
		
		#トピックを配列に追加
		allot_topic_list.append(allot_topic)
		
		#ファイルポインタを次へ
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#HDPトピックの割当
def hdp_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensimのトピックを読み込み(HDP)
	gensim_topic = gensim_lib.load_The_HdpTopic(_topic)
	
	#割当対象のファイル
	allot_file = open(_wakachi_path,"r")
	
	#返却用の変数
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#ファイルの最終行まで繰り返す
	while allot_file_line:
		
		#TABで区切られているわかち書きのテキストを読み込みしトークン化
		allot_file_line_tokens = allot_file_line.split()
		
		#トークン化された単語群をBOWに変換
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#トピックを割り当てトピックの確率分布を取得
		allot_topic = gensim_lib.doc_to_hdptopic_distribution(allot_file_line_bow,gensim_topic)
		
		#トピックを配列に追加
		allot_topic_list.append(allot_topic)
		
		#ファイルポインタを次へ
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#割当トピックの書き込み
def topic_write(_allot_topic_list,_doc_topic_allot_path,_doc_max_allot_path,_topic_num):
	
	#文書番号
	docNum = 0
	
	#トピック分布の書き込み用変数
	doc_topic = defaultdict(lambda:defaultdict(lambda:0))
	
	#最大トピックの書き込み用変数
	doc_title = defaultdict(lambda:0)
	
	#トピック分布の書き込み用ファイル
	doc_topic_allot = open(_doc_topic_allot_path,"w")
	
	#最大トピックの書き込み用ファイル
	doc_max_allot = open(_doc_max_allot_path,"w")
	
	#文書ごとに繰り返す
	for allot_topic in _allot_topic_list:
	
		#トピック番号ごとに繰り返す
		for allot_topic_num,topic_probability in allot_topic:
			doc_topic[docNum][allot_topic_num] = topic_probability
			
		#文書番号を次へ
		docNum += 1
	
	#トピック分布の書き込み
	for d_num in range(0,docNum):
		
		#最大トピック番号まで繰り返す
		for t_num in range(0,_topic_num):
			
			#トピック番号の生成確率を書き込み
			doc_topic_allot.write(str(doc_topic[d_num][t_num]) + "\t")
		
		#改行
		doc_topic_allot.write("\r\n")
	
	#最大トピックの推定、文書ごとに繰り返す
	for d_num in range(0,docNum):
		
		#トピックの生成確率の最小値
		topic_pro = 0
		
		#トピック番号
		max_doc_topic = 10000
		
		#文書番号をファイルに書き込み
		doc_max_allot.write(str(d_num) + "\t:\t")
		
		#トピック番号ごとに繰り返す
		for t_num in doc_topic[d_num]:
			
			#トピック番号の生成確率が最小値より大きい場合
			if math.fabs(doc_topic[d_num][t_num]) > topic_pro:
				
				#文書の最大トピックを更新
				max_doc_topic = t_num
				
				#文書の最大トピックの生成確率を更新
				topic_pro = doc_topic[d_num][t_num]
				
		#最大トピックをファイルに書き込み
		doc_max_allot.write(str(max_doc_topic)  + "\t" + str(topic_pro) + "\r\n")
			
	doc_topic_allot.close()
	doc_max_allot.close()
	
#割当トピックの書き込み
def topic_write_hdp(_allot_topic_list,_doc_topic_allot_path,_doc_max_allot_path,_hpd_max_topic_num):
	
	#文書番号
	docNum = 0
	
	#トピック分布の書き込み用変数
	doc_topic = defaultdict(lambda:defaultdict(lambda:0))
	
	#最大トピックの書き込み用変数
	doc_title = defaultdict(lambda:0)
	
	#トピック分布の書き込み用ファイル
	doc_topic_allot = open(_doc_topic_allot_path,"w")
	
	#最大トピックの書き込み用ファイル
	doc_max_allot = open(_doc_max_allot_path,"w")
	
	#文書ごとに繰り返す
	for allot_topic in _allot_topic_list:
	
		#トピック番号ごとに繰り返す
		for allot_topic_num,topic_probability in allot_topic:
			doc_topic[docNum][allot_topic_num] = topic_probability
			
		#文書番号を次へ
		docNum += 1
	
	#トピック分布の書き込み
	for d_num in range(0,docNum):
		
		#最大トピック番号まで繰り返す
		for t_num in range(0,_hpd_max_topic_num):
			
			#トピック番号の生成確率を書き込み
			doc_topic_allot.write(str(doc_topic[d_num][t_num]) + "\t")
		
		#改行
		doc_topic_allot.write("\r\n")
	
	#最大トピックの推定、文書ごとに繰り返す
	for d_num in range(0,docNum):
		
		#トピックの生成確率の最小値
		topic_pro = 0
		
		#トピック番号
		max_doc_topic = 10000
		
		#文書番号をファイルに書き込み
		doc_max_allot.write(str(d_num) + "\t:\t")
		
		#トピック番号ごとに繰り返す
		for t_num in doc_topic[d_num]:
			
			#トピック番号の生成確率が最小値より大きい場合
			if math.fabs(doc_topic[d_num][t_num]) > topic_pro:
				
				#文書の最大トピックを更新
				max_doc_topic = t_num
				
				#文書の最大トピックの生成確率を更新
				topic_pro = doc_topic[d_num][t_num]
				
		#最大トピックをファイルに書き込み
		doc_max_allot.write(str(max_doc_topic)  + "\t" + str(topic_pro) + "\r\n")
			
	doc_topic_allot.close()
	doc_max_allot.close()
