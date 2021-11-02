# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import similarity
import conf

if __name__ == "__main__":
	print "Start"
	
	#gensim�����̃p�X
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensim�R�[�p�X�̃p�X
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPIC���f���̃p�X
	topic_path = conf.simulation_conf.lsi_gensim_topic_model
	
	#���̓t�@�C���̃p�X
	analyze_file_path = conf.similarity_conf.analyze_file_path
	
	#���̓t�@�C���̏������݃p�X
	similarity_path = conf.similarity_conf.similarity_file_path
	
	#LSI���f���̕ۑ��p�X
	lsi_corpus_path = conf.similarity_conf.lsi_corpa_path
	
	####�����̒P��ID�̊֌W�Ŏ����݂̂����Ŏ����̓Ǎ����s��####
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(dic_path)
	
	#LSI�R�[�p�X�ɕϊ�
	similarity.lsi_corpus_vector_maker(corpa_path,topic_path,lsi_corpus_path)
	
	#���̓t�@�C����LSI�x�N�g���ɕϊ�
	vec_lsi_list = similarity.lsi_search_str_vector(gensim_dic,topic_path,analyze_file_path)
	
	#LSI���f���ɂ�鋗���v�Z�ƃt�@�C���o��
	similarity.lsi_similar_str_vector(lsi_corpus_path,vec_lsi_list,similarity_path)
	
	print "Finished"