# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import similarity
import conf

if __name__ == "__main__":
	print "Start"
	
	#gensim辞書のパス
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensimコーパスのパス
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPICモデルのパス
	topic_path = conf.simulation_conf.lsi_gensim_topic_model
	
	#分析ファイルのパス
	analyze_file_path = conf.similarity_conf.analyze_file_path
	
	#分析ファイルの書き込みパス
	similarity_path = conf.similarity_conf.similarity_file_path
	
	#LSIモデルの保存パス
	lsi_corpus_path = conf.similarity_conf.lsi_corpa_path
	
	####辞書の単語IDの関係で辞書のみここで辞書の読込を行う####
	#gensimの辞書を読み込み
	gensim_dic = gensim_lib.load_The_GensimDic(dic_path)
	
	#LSIコーパスに変換
	similarity.lsi_corpus_vector_maker(corpa_path,topic_path,lsi_corpus_path)
	
	#分析ファイルをLSIベクトルに変換
	vec_lsi_list = similarity.lsi_search_str_vector(gensim_dic,topic_path,analyze_file_path)
	
	#LSIモデルによる距離計算とファイル出力
	similarity.lsi_similar_str_vector(lsi_corpus_path,vec_lsi_list,similarity_path)
	
	print "Finished"