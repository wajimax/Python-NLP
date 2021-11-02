# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import numpy
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#トピック割当対象となるわかち書きファイルのパス
	file_path = conf.simulation_conf.wakachi_fileName_path
	
	#gensim辞書のパス
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensimコーパスのパス
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPICモデルの保存パス
	topic_path = conf.simulation_conf.hdp_gensim_topic_model
	
	#割当TOPICの書き込みパス
	doc_topic_allot_path = conf.simulation_conf.hdp_gensim_topic_allot
	
	#割当最大TOPICの書き込みパス
	doc_max_allot_path = conf.simulation_conf.hdp_gensim_topic_max_allot
	
	#最大トピック数の取得
	hpd_max_topic_num = sum(1 for line in open(conf.simulation_conf.hdp_gensim_topic_probability))
	
	#TOPICの割当
	allot_topic_list = topic.hdp_topic_allot(file_path,dic_path,corpa_path,topic_path)
	
	#割当TOPICの書き込み
	topic.topic_write_hdp(allot_topic_list,doc_topic_allot_path,doc_max_allot_path,hpd_max_topic_num)
	
	print "Finished"