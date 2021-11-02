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
	
	#gensim�����̃p�X
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensim�R�[�p�X�̃p�X
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPIC���f���̕ۑ��p�X
	topic_path = conf.simulation_conf.lda_gensim_topic_model
	
	#TOPIC���o
	lda_topic = topic.lda_maker(dic_path,corpa_path,topic_path,topicNum)
	
	#�g�s�b�N�����X�g�^�ɒ��o
	lda_extraction = topic.topic_to_list(lda_topic)
	
	print "write file"
	
	#�P�ꕪ�z�̕ۑ��p
	ja_lda_file_words = open(conf.simulation_conf.lda_gensim_topic_words,"w")
	
	#�����m���̕ۑ��p
	ja_lda_file_probability = open(conf.simulation_conf.lda_gensim_topic_probability,"w")
	
	#�t�@�C�����o(�P�ꕪ�z)
	for topic_str in lda_extraction[0]:
		topic_str.strip()
		ja_lda_file_words.writelines("%s\r\n" % (topic_str))
		
	#�t�@�C�����o(�����m��)
	for topic_probability in lda_extraction[1]:
		ja_lda_file_probability.writelines("%s\r\n" % (topic_probability))
	
	#�t�@�C���|�C���^�����
	ja_lda_file_words.close()
	ja_lda_file_probability.close()
	
	print "Finished"