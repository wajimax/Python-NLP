# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#トピック数
	topicNum = conf.simulation_conf.topicNum
	
	#トピック割当対象となるわかち書きファイルのパス
	file_path = conf.simulation_conf.wakachi_fileName_path
	
	#gensim辞書のパス
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensimコーパスのパス
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPICモデルの保存パス
	topic_path = conf.simulation_conf.lda_gensim_topic_model
	
	#割当TOPICの書き込みパス
	doc_topic_allot_path = conf.simulation_conf.lda_gensim_topic_allot
	
	#割当最大TOPICの書き込みパス
	doc_max_allot_path = conf.simulation_conf.lda_gensim_topic_max_allot
	
	#TOPICの割当
	allot_topic_list = topic.lda_topic_allot(file_path,dic_path,corpa_path,topic_path)
	
	#割当TOPICの書き込み
	topic.topic_write(allot_topic_list,doc_topic_allot_path,doc_max_allot_path,topicNum)
	
	print "Finished"