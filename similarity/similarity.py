# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import conf
import math
from collections import defaultdict

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#コーパスをLSIモデルに変換
def lsi_corpus_vector_maker(_gensim_corpa_path,_topic_path,_lsi_corpus_path):
	
	#gensimのコーパスを読み込み
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensimのトピックを読み込み(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic_path)
	
	#コーパスの変換
	index = gensim_lib.lsi_convert_corpus(gensim_corpa,gensim_topic)
	
	#コーパスを保存
	gensim_lib.store_The_lsi_corpus(index,_lsi_corpus_path)
	
#入力クエリをLSIモデルに変換し距離を算出
def lsi_search_str_vector(_dictionary,_topic_path,_analyze_file_path):
	
	#gensimのトピックを読み込み(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic_path)
	
	#分析ファイルを読み込み
	analyze_file = open(_analyze_file_path,"r")
	
	#分析ファイルの読み込み
	analyze_file_line = analyze_file.readline()
	
	#分析ファイル
	vec_lsi_list = []
	
	#分析ファイルの終わりまで繰り返す
	while analyze_file_line:
		
			#入力クエリをLSIベクトル空間に変換
			vec_lsi = gensim_lib.lsi_convert_queries(_dictionary,gensim_topic,analyze_file_line)
			
			#分析ファイルリスト
			vec_lsi_list.append(vec_lsi)
			
			#分析ファイルの読み込み
			analyze_file_line = analyze_file.readline()
			
	return vec_lsi_list
	
#距離計算
def lsi_similar_str_vector(_lsi_corpus_path,_vec_lsi_list,_similarity_path):
	
	#LSIコーパスを読込
	index = gensim_lib.load_The_lsi_corpus(_lsi_corpus_path)
	
	#距離計算用の書き込みファイル
	similarity_file = open(_similarity_path,"w")
	
	#距離計算用の配列
	sims_list = defaultdict(lambda:defaultdict(lambda:0))
	
	#距離計算用の番号
	vec_num = 0
	doc_num = 0
	
	#print len(_vec_lsi_list)
	
	#距離計算
	for vec_lsi in _vec_lsi_list:
		
		#入力クエリとLSIベクトル空間上の距離を算出
		sims = index[vec_lsi]
		
		#距離計算用
		for sim in list(enumerate(sims)):
			
			#類似度
			sims_list[vec_num][doc_num] = sim[1]
			
			doc_num = doc_num + 1
		
		#インクリメント
		doc_num = 0
		vec_num = vec_num + 1
		
	vec_num = 0
	doc_num = 0
	
	
	#ドキュメントリストの間繰り返す
	while len(sims_list[0]) > doc_num:
		
		#距離計算リストの間繰り返す
		while len(sims_list) > vec_num:
			
			#列に距離計算の文字がくるようにする
			similarity_file.write(str(sims_list[vec_num][doc_num]) + "\t")
			
			vec_num = vec_num + 1
		
		#改行
		similarity_file.write("\r\n")
		
		vec_num = 0
		doc_num = doc_num + 1
	
	similarity_file.close()
	
##word2vecのモデルを作成##
def word2vec_model_maker(_wakachi_path,_store_path):
	
	#わかち書きファイルをword2vecインスタンスに変換
	model = gensim_lib.tokens_To_Word2Vec(_wakachi_path)
	
	#モデルを保存
	gensim_lib.store_The_Word2Vec(model,_store_path)
	
##word2vecモデルを使用して類似度を算出##
##Inputは1行のtab区切りのデータと想定##
def word2vec_similar_calculation(_model_path,_analyze_file_path,_wordNum,_similarity_path):
	
	#word2vecコーパスを読込
	model = gensim_lib.load_The_Word2Vec(_model_path)
	
	#分析対象のファイルを読込
	analyze_file = open(_analyze_file_path,"r")
	
	#距離計算用の書き込みファイル
	similarity_file = open(_similarity_path,"w")
	
	#距離計算用の配列
	sims_list = defaultdict(lambda:0)
	
	#分析ファイルの読み込み
	analyze_file_word_list = analyze_file.readline().split()
	
	#文書番号
	doc_num = 0
	
	#分析ファイルの終わりまで繰り返す
	for analyze_file_word in analyze_file_word_list:
			
		similarity_file.write(analyze_file_word + "\r\n")
		
		#入力単語に対する類似度を出力
		sim_list = gensim_lib.word_To_Word2Vec_list(analyze_file_word,model,_wordNum)
		
		print sim_list
		
		#スコアの書き込み
		for sim_list_word,sim_list_score in sim_list:
			
			#単語
			similarity_file.write(sim_list_word + "\t")
		
		#改行
		similarity_file.write("\r\n")
			
		#類似単語の類似度の書き込み
		for sim_list_word,sim_list_score in sim_list:
				
			#スコア
			similarity_file.write(str(sim_list_score) + "\t")
			
		#改行
		similarity_file.write("\r\n\r\n")

	#ファイルポインタのクローズ
	analyze_file.close()
	similarity_file.close()
	
##word2vecモデルを元にして辞書を作成##
def extended_dictionary_calculation(_model_path,_analyze_file_path,_wordNum,_similarity_path):
	
	#word2vecコーパスを読込
	model = gensim_lib.load_The_Word2Vec(_model_path)
	
	#分析対象のファイルを読込
	analyze_file = open(_analyze_file_path,"r")
	
	#距離計算用の書き込みファイル
	similarity_file = open(_similarity_path,"w")
	
	#1行読み込み
	analyze_file_line = analyze_file.readline().rstrip()
	
	#ファイルの最終行まで繰り返す
	while analyze_file_line:
		
		#区切り文字の[:]で分割する
		#優れる:すぐれる:動詞:1
		dic_list = analyze_file_line.split(":")
		
		#元の辞書の単語書き込み
		similarity_file.write(dic_list[0] + ":" + dic_list[1] + "\r\n")
		
		#入力単語に対する類似度を出力
		sim_list = gensim_lib.word_To_Word2Vec_list(dic_list[0],model,_wordNum)
		
		#スコアの書き込み
		for sim_list_word,sim_list_score in sim_list:
			
			if(len(sim_list_word.rstrip()) > 0):
				
				#単語 + 極性値
				similarity_file.write(sim_list_word + ":" + dic_list[1] + "\r\n")
			
		#分析ファイルの読み込み
		analyze_file_line = analyze_file.readline().rstrip()
			
	#ファイルポインタのクローズ
	analyze_file.close()
	similarity_file.close()
	
##doc2vecのモデルを作成##
def doc2vec_model_maker(_wakachi_path,_store_path):
	
	#わかち書きファイルをword2vecインスタンスに変換
	model = gensim_lib.tokens_To_Doc2Vec(_wakachi_path)
	
	#モデルを保存
	gensim_lib.store_The_Doc2Vec(model,_store_path)