# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#トピック数(LSIの場合は次元数のためlsi_kを使用)
	topicNum = conf.simulation_conf.lsi_k
	
	#gensim辞書のパス
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensimコーパスのパス
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPICモデルの保存パス
	topic_path = conf.simulation_conf.lsi_gensim_topic_model
	
	#TOPIC抽出
	lsi_topic = topic.lsi_maker(dic_path,corpa_path,topic_path,topicNum)
	
	#トピックをリスト型に抽出
	lsi_extraction = topic.topic_to_list(lsi_topic)
	
	print "write file"
	
	#単語分布の保存用
	ja_lsi_file_words = open(conf.simulation_conf.lsi_gensim_topic_words,"w")
	
	#生成確率の保存用
	ja_lsi_file_probability = open(conf.simulation_conf.lsi_gensim_topic_probability,"w")
	
	#ファイル抽出(単語分布)
	for topic_str in lsi_extraction[0]:
		topic_str.strip()
		ja_lsi_file_words.writelines("%s\r\n" % (topic_str))
		
	#ファイル抽出(生成確率)
	for topic_probability in lsi_extraction[1]:
		ja_lsi_file_probability.writelines("%s\r\n" % (topic_probability))
	
	#ファイルポインタを閉じる
	ja_lsi_file_words.close()
	ja_lsi_file_probability.close()
	
	print "Finished"