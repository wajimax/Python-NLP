# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#gensim�����̃p�X
	dic_path = conf.simulation_conf.gensim_dic_path
	
	#gensim�R�[�p�X�̃p�X
	corpa_path = conf.simulation_conf.gensim_corpa_path
	
	#TOPIC���f���̕ۑ��p�X
	topic_path = conf.simulation_conf.hdp_gensim_topic_model
	
	#TOPIC���o
	hdp_topic = topic.hdp_maker(dic_path,corpa_path,topic_path)
	
	#�g�s�b�N�����X�g�^�ɒ��o
	hdp_extraction = topic.topic_to_list_hdp(hdp_topic)
	
	print "write file"
	
	#�P�ꕪ�z�̕ۑ��p
	ja_hdp_file_words = open(conf.simulation_conf.hdp_gensim_topic_words,"w")
	
	#�����m���̕ۑ��p
	ja_hdp_file_probability = open(conf.simulation_conf.hdp_gensim_topic_probability,"w")
	
	#�t�@�C�����o(�P�ꕪ�z)
	for topic_str in hdp_extraction[0]:
		topic_str.strip()
		ja_hdp_file_words.writelines("%s\r\n" % (topic_str))
	
	#�t�@�C�����o(�����m��)
	for topic_probability in hdp_extraction[1]:
		ja_hdp_file_probability.writelines("%s\r\n" % (topic_probability))
	
	#�t�@�C���|�C���^�����
	ja_hdp_file_words.close()
	ja_hdp_file_probability.close()
	
	print "Finished"