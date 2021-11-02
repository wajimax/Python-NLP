# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import conf
import math
from collections import defaultdict

#gensim�̎����E�R�[�p�X�̍쐬
def topic_corpus_maker(_fileName,_input_filepath,_output_filepath):
	
	#�����̕ۑ��p�X
	gensim_dic_path = _output_filepath + _fileName + "_gensimdic"
	
	#�R�[�p�X�̕ۑ��p�X
	gensim_corpa_path = _output_filepath + _fileName + "_gensimcorpa"
	
	filepath = _input_filepath + _fileName
	
	print filepath
	
	#�t�@�C���̓ǂݍ���
	ja_file = open(filepath,"r")
	
	#�ԋp�l�p�̔z��
	ja_list = []
	
	#1�s�ڂ̓ǂݍ���
	ja_line = ja_file.readline()
	
	#�t�@�C���̍ŏI�s�܂ŌJ��Ԃ�
	while ja_line:
		
		#TAB�ŋ�؂��Ă���킩�������̃e�L�X�g��ǂݍ���
		ja_line_tokens = ja_line.split("\t")
		
		#�񎟌��z��Ɋi�[
		ja_list.append(ja_line_tokens)
		
		#�t�@�C���|�C���^������
		ja_line = ja_file.readline()
		
	#�t�@�C���|�C���^���N���[�Y
	ja_file.close()
	
	#�񎟌��z�������gensim�̎������쐬
	gensim_dic = gensim_lib.tokens_To_GensimDic(ja_list)
	
	#gensim�̎������T�[�o�ɕۑ�
	gensim_lib.store_The_GensimDic(gensim_dic,gensim_dic_path)
	
	#�񎟌��z�������gensim�̃R�[�p�X���쐬
	gensim_corpa = gensim_lib.tokens_To_GensimCorpus(ja_list,gensim_dic)
	
	#gensim�̃R�[�p�X��ۑ�
	gensim_lib.store_The_GensimCorpus(gensim_corpa,gensim_corpa_path)
	

#LDA�g�s�b�N�̒��o
def lda_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path,_topic_num):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#LDA�g�s�b�N�𒊏o
	lda_topic = gensim_lib.extraction_LdaTopic(gensim_dic,gensim_corpa,_topic_num)
	
	#LDA�g�s�b�N��ۑ�
	gensim_lib.store_The_LdaTopic(lda_topic,_topic_path)
	
	return lda_topic
	
#LSI�g�s�b�N�̒��o
def lsi_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path,_topic_num):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#TF-IDF�̃C���X�^���X�쐬
	gensim_tfidf_instance = gensim_lib.gensimCorpus_To_TfidfInstance(gensim_corpa)
	
	#TF-IDF�̃R�[�p�X���쐬
	gensim_tfidf_corpa = gensim_lib.gensimCorpus_To_TfidfCorpus(gensim_corpa,gensim_tfidf_instance)
	
	#LSI�g�s�b�N�𒊏o
	lsi_topic = gensim_lib.extraction_LsiTopic(gensim_dic,gensim_tfidf_corpa,_topic_num)
	
	#LSI�g�s�b�N��ۑ�
	gensim_lib.store_The_LsiTopic(lsi_topic,_topic_path)
	
	return lsi_topic
	
#HDP�g�s�b�N�̏o��
def hdp_maker(_gensim_dic_path,_gensim_corpa_path,_topic_path):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#HDP�g�s�b�N�𒊏o
	hdp_topic = gensim_lib.extraction_HdpTopic(gensim_dic,gensim_corpa)
	
	#HDP�g�s�b�N��ۑ�
	gensim_lib.store_The_HdpTopic(hdp_topic,_topic_path)
	
	#���o����HDP�g�s�b�N�̈ꕔ�𒊏o
	#hdp_topic_extract = hdp_topic.print_topics(topics=_topic_num, topn=10)
	hdp_topic_extract = hdp_topic.print_topics(topics=-1, topn=10)
	
	return hdp_topic_extract
	
#�g�s�b�N�e�L�X�g�̕ۑ�
def topic_to_list(_topic):
	
	#�P�ꕪ�z�Əo���m���̃��X�g
	extraction_list = []
	word_list = []
	probability_list = []
	
	for topic in _topic.show_topics(-1):
		print topic
		#topic.strip()
		#topic_list = topic.split('+')
		#2018/10/13
		topic_str = topic[1].strip()
		topic_list = topic_str.split('+')
		topic_word_line = ""
		topic_probability_line = ""
		
		for topic_line in topic_list:
			topic_line.strip()
			topic_element = topic_line.split('*')
			topic_word_line = topic_word_line + topic_element[1]
			topic_probability_line = topic_probability_line + topic_element[0]
			
		word_list.append(topic_word_line)
		probability_list.append(topic_probability_line)
		
		extraction_list.append(word_list)
		extraction_list.append(probability_list)
	
	return extraction_list
	
#�g�s�b�N�e�L�X�g�̕ۑ�(HDP)
def topic_to_list_hdp(_topic):
	
	#�P�ꕪ�z�Əo���m���̃��X�g
	extraction_list = []
	word_list = []
	probability_list = []
	
	for topic in _topic:
		print topic
		topic.strip()
		topic_list = topic.split('+')
		topic_word_line = ""
		topic_probability_line = ""
		
		for topic_line in topic_list:
			topic_line.strip()
			topic_element = topic_line.split('*')
			topic_word_line = topic_word_line + topic_element[1]
			topic_probability_line = topic_probability_line + topic_element[0]
			
		word_list.append(topic_word_line)
		probability_list.append(topic_probability_line)
		
		extraction_list.append(word_list)
		extraction_list.append(probability_list)
	
	return extraction_list

#LDA�g�s�b�N�̊���
def lda_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensim�̃g�s�b�N��ǂݍ���(LDA)
	gensim_topic = gensim_lib.load_The_LdaTopic(_topic)
	
	#�����Ώۂ̃t�@�C��
	allot_file = open(_wakachi_path,"r")
	
	#�ԋp�p�̕ϐ�
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#�t�@�C���̍ŏI�s�܂ŌJ��Ԃ�
	while allot_file_line:
		
		#TAB�ŋ�؂��Ă���킩�������̃e�L�X�g��ǂݍ��݂��g�[�N����
		allot_file_line_tokens = allot_file_line.split()
		
		#�g�[�N�������ꂽ�P��Q��BOW�ɕϊ�
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#�g�s�b�N�����蓖�ăg�s�b�N�̊m�����z���擾
		allot_topic = gensim_lib.doc_to_ldatopic_distribution(allot_file_line_bow,gensim_topic)
		
		#�g�s�b�N��z��ɒǉ�
		allot_topic_list.append(allot_topic)
		
		#�t�@�C���|�C���^������
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#LSI�g�s�b�N�̊���
def lsi_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensim�̃g�s�b�N��ǂݍ���(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic)
	
	#�����Ώۂ̃t�@�C��
	allot_file = open(_wakachi_path,"r")
	
	#�ԋp�p�̕ϐ�
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#�t�@�C���̍ŏI�s�܂ŌJ��Ԃ�
	while allot_file_line:
		
		#TAB�ŋ�؂��Ă���킩�������̃e�L�X�g��ǂݍ��݂��g�[�N����
		allot_file_line_tokens = allot_file_line.split()
		
		#�g�[�N�������ꂽ�P��Q��BOW�ɕϊ�
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#�g�s�b�N�����蓖�ăg�s�b�N�̊m�����z���擾
		allot_topic = gensim_lib.doc_to_lsitopic_distribution(allot_file_line_bow,gensim_topic)
		
		#�g�s�b�N��z��ɒǉ�
		allot_topic_list.append(allot_topic)
		
		#�t�@�C���|�C���^������
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#HDP�g�s�b�N�̊���
def hdp_topic_allot(_wakachi_path,_gensim_dic_path,_gensim_corpa_path,_topic):
	
	#gensim�̎�����ǂݍ���
	gensim_dic = gensim_lib.load_The_GensimDic(_gensim_dic_path)
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensim�̃g�s�b�N��ǂݍ���(HDP)
	gensim_topic = gensim_lib.load_The_HdpTopic(_topic)
	
	#�����Ώۂ̃t�@�C��
	allot_file = open(_wakachi_path,"r")
	
	#�ԋp�p�̕ϐ�
	allot_topic_list = []
	
	allot_file_line = allot_file.readline()
	
	#�t�@�C���̍ŏI�s�܂ŌJ��Ԃ�
	while allot_file_line:
		
		#TAB�ŋ�؂��Ă���킩�������̃e�L�X�g��ǂݍ��݂��g�[�N����
		allot_file_line_tokens = allot_file_line.split()
		
		#�g�[�N�������ꂽ�P��Q��BOW�ɕϊ�
		allot_file_line_bow = gensim_dic.doc2bow(allot_file_line_tokens)
		
		#�g�s�b�N�����蓖�ăg�s�b�N�̊m�����z���擾
		allot_topic = gensim_lib.doc_to_hdptopic_distribution(allot_file_line_bow,gensim_topic)
		
		#�g�s�b�N��z��ɒǉ�
		allot_topic_list.append(allot_topic)
		
		#�t�@�C���|�C���^������
		allot_file_line = allot_file.readline()
	
	return allot_topic_list

#�����g�s�b�N�̏�������
def topic_write(_allot_topic_list,_doc_topic_allot_path,_doc_max_allot_path,_topic_num):
	
	#�����ԍ�
	docNum = 0
	
	#�g�s�b�N���z�̏������ݗp�ϐ�
	doc_topic = defaultdict(lambda:defaultdict(lambda:0))
	
	#�ő�g�s�b�N�̏������ݗp�ϐ�
	doc_title = defaultdict(lambda:0)
	
	#�g�s�b�N���z�̏������ݗp�t�@�C��
	doc_topic_allot = open(_doc_topic_allot_path,"w")
	
	#�ő�g�s�b�N�̏������ݗp�t�@�C��
	doc_max_allot = open(_doc_max_allot_path,"w")
	
	#�������ƂɌJ��Ԃ�
	for allot_topic in _allot_topic_list:
	
		#�g�s�b�N�ԍ����ƂɌJ��Ԃ�
		for allot_topic_num,topic_probability in allot_topic:
			doc_topic[docNum][allot_topic_num] = topic_probability
			
		#�����ԍ�������
		docNum += 1
	
	#�g�s�b�N���z�̏�������
	for d_num in range(0,docNum):
		
		#�ő�g�s�b�N�ԍ��܂ŌJ��Ԃ�
		for t_num in range(0,_topic_num):
			
			#�g�s�b�N�ԍ��̐����m������������
			doc_topic_allot.write(str(doc_topic[d_num][t_num]) + "\t")
		
		#���s
		doc_topic_allot.write("\r\n")
	
	#�ő�g�s�b�N�̐���A�������ƂɌJ��Ԃ�
	for d_num in range(0,docNum):
		
		#�g�s�b�N�̐����m���̍ŏ��l
		topic_pro = 0
		
		#�g�s�b�N�ԍ�
		max_doc_topic = 10000
		
		#�����ԍ����t�@�C���ɏ�������
		doc_max_allot.write(str(d_num) + "\t:\t")
		
		#�g�s�b�N�ԍ����ƂɌJ��Ԃ�
		for t_num in doc_topic[d_num]:
			
			#�g�s�b�N�ԍ��̐����m�����ŏ��l���傫���ꍇ
			if math.fabs(doc_topic[d_num][t_num]) > topic_pro:
				
				#�����̍ő�g�s�b�N���X�V
				max_doc_topic = t_num
				
				#�����̍ő�g�s�b�N�̐����m�����X�V
				topic_pro = doc_topic[d_num][t_num]
				
		#�ő�g�s�b�N���t�@�C���ɏ�������
		doc_max_allot.write(str(max_doc_topic)  + "\t" + str(topic_pro) + "\r\n")
			
	doc_topic_allot.close()
	doc_max_allot.close()
	
#�����g�s�b�N�̏�������
def topic_write_hdp(_allot_topic_list,_doc_topic_allot_path,_doc_max_allot_path,_hpd_max_topic_num):
	
	#�����ԍ�
	docNum = 0
	
	#�g�s�b�N���z�̏������ݗp�ϐ�
	doc_topic = defaultdict(lambda:defaultdict(lambda:0))
	
	#�ő�g�s�b�N�̏������ݗp�ϐ�
	doc_title = defaultdict(lambda:0)
	
	#�g�s�b�N���z�̏������ݗp�t�@�C��
	doc_topic_allot = open(_doc_topic_allot_path,"w")
	
	#�ő�g�s�b�N�̏������ݗp�t�@�C��
	doc_max_allot = open(_doc_max_allot_path,"w")
	
	#�������ƂɌJ��Ԃ�
	for allot_topic in _allot_topic_list:
	
		#�g�s�b�N�ԍ����ƂɌJ��Ԃ�
		for allot_topic_num,topic_probability in allot_topic:
			doc_topic[docNum][allot_topic_num] = topic_probability
			
		#�����ԍ�������
		docNum += 1
	
	#�g�s�b�N���z�̏�������
	for d_num in range(0,docNum):
		
		#�ő�g�s�b�N�ԍ��܂ŌJ��Ԃ�
		for t_num in range(0,_hpd_max_topic_num):
			
			#�g�s�b�N�ԍ��̐����m������������
			doc_topic_allot.write(str(doc_topic[d_num][t_num]) + "\t")
		
		#���s
		doc_topic_allot.write("\r\n")
	
	#�ő�g�s�b�N�̐���A�������ƂɌJ��Ԃ�
	for d_num in range(0,docNum):
		
		#�g�s�b�N�̐����m���̍ŏ��l
		topic_pro = 0
		
		#�g�s�b�N�ԍ�
		max_doc_topic = 10000
		
		#�����ԍ����t�@�C���ɏ�������
		doc_max_allot.write(str(d_num) + "\t:\t")
		
		#�g�s�b�N�ԍ����ƂɌJ��Ԃ�
		for t_num in doc_topic[d_num]:
			
			#�g�s�b�N�ԍ��̐����m�����ŏ��l���傫���ꍇ
			if math.fabs(doc_topic[d_num][t_num]) > topic_pro:
				
				#�����̍ő�g�s�b�N���X�V
				max_doc_topic = t_num
				
				#�����̍ő�g�s�b�N�̐����m�����X�V
				topic_pro = doc_topic[d_num][t_num]
				
		#�ő�g�s�b�N���t�@�C���ɏ�������
		doc_max_allot.write(str(max_doc_topic)  + "\t" + str(topic_pro) + "\r\n")
			
	doc_topic_allot.close()
	doc_max_allot.close()
