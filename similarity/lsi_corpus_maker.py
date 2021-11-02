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
	
	#LSIモデルの保存パス
	lsi_corpus_path = conf.similarity_conf.lsi_corpa_path
	
	print "write file"
	
	#LSIコーパスに変換
	similarity.lsi_corpus_vector_maker(dic_path,corpa_path,topic_path,lsi_corpus_path)
	
	print "Finished"