# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#gensim辞書のパス
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensimコーパスのパス
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPICモデルの保存パス
	topic_path = conf.simulation_conf.hdp_gensim_topic_model
	
	#TOPIC抽出
	hdp_topic = topic.hdp_maker(dic_path,corpa_path,topic_path)
	
	#トピックをリスト型に抽出
	hdp_extraction = topic.topic_to_list_hdp(hdp_topic)
	
	print "write file"
	
	#単語分布の保存用
	ja_hdp_file_words = open(conf.simulation_conf.hdp_gensim_topic_words,"w")
	
	#生成確率の保存用
	ja_hdp_file_probability = open(conf.simulation_conf.hdp_gensim_topic_probability,"w")
	
	#ファイル抽出(単語分布)
	for topic_str in hdp_extraction[0]:
		topic_str.strip()
		ja_hdp_file_words.writelines("%s\r\n" % (topic_str))
	
	#ファイル抽出(生成確率)
	for topic_probability in hdp_extraction[1]:
		ja_hdp_file_probability.writelines("%s\r\n" % (topic_probability))
	
	#ファイルポインタを閉じる
	ja_hdp_file_words.close()
	ja_hdp_file_probability.close()
	
	print "Finished"