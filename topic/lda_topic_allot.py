# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#�g�s�b�N��
	topicNum = conf.simulation_conf.topicNum
	
	#�g�s�b�N�����ΏۂƂȂ�킩�������t�@�C���̃p�X
	file_path = conf.simulation_conf.wakachi_fileName_path
	
	#gensim�����̃p�X
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensim�R�[�p�X�̃p�X
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPIC���f���̕ۑ��p�X
	topic_path = conf.simulation_conf.lda_gensim_topic_model
	
	#����TOPIC�̏������݃p�X
	doc_topic_allot_path = conf.simulation_conf.lda_gensim_topic_allot
	
	#�����ő�TOPIC�̏������݃p�X
	doc_max_allot_path = conf.simulation_conf.lda_gensim_topic_max_allot
	
	#TOPIC�̊���
	allot_topic_list = topic.lda_topic_allot(file_path,dic_path,corpa_path,topic_path)
	
	#����TOPIC�̏�������
	topic.topic_write(allot_topic_list,doc_topic_allot_path,doc_max_allot_path,topicNum)
	
	print "Finished"