# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import conf
import math
from collections import defaultdict

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#�R�[�p�X��LSI���f���ɕϊ�
def lsi_corpus_vector_maker(_gensim_corpa_path,_topic_path,_lsi_corpus_path):
	
	#gensim�̃R�[�p�X��ǂݍ���
	gensim_corpa = gensim_lib.load_The_GensimCorpus(_gensim_corpa_path)
	
	#gensim�̃g�s�b�N��ǂݍ���(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic_path)
	
	#�R�[�p�X�̕ϊ�
	index = gensim_lib.lsi_convert_corpus(gensim_corpa,gensim_topic)
	
	#�R�[�p�X��ۑ�
	gensim_lib.store_The_lsi_corpus(index,_lsi_corpus_path)
	
#���̓N�G����LSI���f���ɕϊ����������Z�o
def lsi_search_str_vector(_dictionary,_topic_path,_analyze_file_path):
	
	#gensim�̃g�s�b�N��ǂݍ���(LSI)
	gensim_topic = gensim_lib.load_The_LsiTopic(_topic_path)
	
	#���̓t�@�C����ǂݍ���
	analyze_file = open(_analyze_file_path,"r")
	
	#���̓t�@�C���̓ǂݍ���
	analyze_file_line = analyze_file.readline()
	
	#���̓t�@�C��
	vec_lsi_list = []
	
	#���̓t�@�C���̏I���܂ŌJ��Ԃ�
	while analyze_file_line:
		
			#���̓N�G����LSI�x�N�g����Ԃɕϊ�
			vec_lsi = gensim_lib.lsi_convert_queries(_dictionary,gensim_topic,analyze_file_line)
			
			#���̓t�@�C�����X�g
			vec_lsi_list.append(vec_lsi)
			
			#���̓t�@�C���̓ǂݍ���
			analyze_file_line = analyze_file.readline()
			
	return vec_lsi_list
	
#�����v�Z
def lsi_similar_str_vector(_lsi_corpus_path,_vec_lsi_list,_similarity_path):
	
	#LSI�R�[�p�X��Ǎ�
	index = gensim_lib.load_The_lsi_corpus(_lsi_corpus_path)
	
	#�����v�Z�p�̏������݃t�@�C��
	similarity_file = open(_similarity_path,"w")
	
	#�����v�Z�p�̔z��
	sims_list = defaultdict(lambda:defaultdict(lambda:0))
	
	#�����v�Z�p�̔ԍ�
	vec_num = 0
	doc_num = 0
	
	#print len(_vec_lsi_list)
	
	#�����v�Z
	for vec_lsi in _vec_lsi_list:
		
		#���̓N�G����LSI�x�N�g����ԏ�̋������Z�o
		sims = index[vec_lsi]
		
		#�����v�Z�p
		for sim in list(enumerate(sims)):
			
			#�ގ��x
			sims_list[vec_num][doc_num] = sim[1]
			
			doc_num = doc_num + 1
		
		#�C���N�������g
		doc_num = 0
		vec_num = vec_num + 1
		
	vec_num = 0
	doc_num = 0
	
	
	#�h�L�������g���X�g�̊ԌJ��Ԃ�
	while len(sims_list[0]) > doc_num:
		
		#�����v�Z���X�g�̊ԌJ��Ԃ�
		while len(sims_list) > vec_num:
			
			#��ɋ����v�Z�̕���������悤�ɂ���
			similarity_file.write(str(sims_list[vec_num][doc_num]) + "\t")
			
			vec_num = vec_num + 1
		
		#���s
		similarity_file.write("\r\n")
		
		vec_num = 0
		doc_num = doc_num + 1
	
	similarity_file.close()
	
##word2vec�̃��f�����쐬##
def word2vec_model_maker(_wakachi_path,_store_path):
	
	#�킩�������t�@�C����word2vec�C���X�^���X�ɕϊ�
	model = gensim_lib.tokens_To_Word2Vec(_wakachi_path)
	
	#���f����ۑ�
	gensim_lib.store_The_Word2Vec(model,_store_path)
	
##word2vec���f�����g�p���ėގ��x���Z�o##
##Input��1�s��tab��؂�̃f�[�^�Ƒz��##
def word2vec_similar_calculation(_model_path,_analyze_file_path,_wordNum,_similarity_path):
	
	#word2vec�R�[�p�X��Ǎ�
	model = gensim_lib.load_The_Word2Vec(_model_path)
	
	#���͑Ώۂ̃t�@�C����Ǎ�
	analyze_file = open(_analyze_file_path,"r")
	
	#�����v�Z�p�̏������݃t�@�C��
	similarity_file = open(_similarity_path,"w")
	
	#�����v�Z�p�̔z��
	sims_list = defaultdict(lambda:0)
	
	#���̓t�@�C���̓ǂݍ���
	analyze_file_word_list = analyze_file.readline().split()
	
	#�����ԍ�
	doc_num = 0
	
	#���̓t�@�C���̏I���܂ŌJ��Ԃ�
	for analyze_file_word in analyze_file_word_list:
			
		similarity_file.write(analyze_file_word + "\r\n")
		
		#���͒P��ɑ΂���ގ��x���o��
		sim_list = gensim_lib.word_To_Word2Vec_list(analyze_file_word,model,_wordNum)
		
		print sim_list
		
		#�X�R�A�̏�������
		for sim_list_word,sim_list_score in sim_list:
			
			#�P��
			similarity_file.write(sim_list_word + "\t")
		
		#���s
		similarity_file.write("\r\n")
			
		#�ގ��P��̗ގ��x�̏�������
		for sim_list_word,sim_list_score in sim_list:
				
			#�X�R�A
			similarity_file.write(str(sim_list_score) + "\t")
			
		#���s
		similarity_file.write("\r\n\r\n")

	#�t�@�C���|�C���^�̃N���[�Y
	analyze_file.close()
	similarity_file.close()
	
##word2vec���f�������ɂ��Ď������쐬##
def extended_dictionary_calculation(_model_path,_analyze_file_path,_wordNum,_similarity_path):
	
	#word2vec�R�[�p�X��Ǎ�
	model = gensim_lib.load_The_Word2Vec(_model_path)
	
	#���͑Ώۂ̃t�@�C����Ǎ�
	analyze_file = open(_analyze_file_path,"r")
	
	#�����v�Z�p�̏������݃t�@�C��
	similarity_file = open(_similarity_path,"w")
	
	#1�s�ǂݍ���
	analyze_file_line = analyze_file.readline().rstrip()
	
	#�t�@�C���̍ŏI�s�܂ŌJ��Ԃ�
	while analyze_file_line:
		
		#��؂蕶����[:]�ŕ�������
		#�D���:�������:����:1
		dic_list = analyze_file_line.split(":")
		
		#���̎����̒P�ꏑ������
		similarity_file.write(dic_list[0] + ":" + dic_list[1] + "\r\n")
		
		#���͒P��ɑ΂���ގ��x���o��
		sim_list = gensim_lib.word_To_Word2Vec_list(dic_list[0],model,_wordNum)
		
		#�X�R�A�̏�������
		for sim_list_word,sim_list_score in sim_list:
			
			if(len(sim_list_word.rstrip()) > 0):
				
				#�P�� + �ɐ��l
				similarity_file.write(sim_list_word + ":" + dic_list[1] + "\r\n")
			
		#���̓t�@�C���̓ǂݍ���
		analyze_file_line = analyze_file.readline().rstrip()
			
	#�t�@�C���|�C���^�̃N���[�Y
	analyze_file.close()
	similarity_file.close()
	
##doc2vec�̃��f�����쐬##
def doc2vec_model_maker(_wakachi_path,_store_path):
	
	#�킩�������t�@�C����word2vec�C���X�^���X�ɕϊ�
	model = gensim_lib.tokens_To_Doc2Vec(_wakachi_path)
	
	#���f����ۑ�
	gensim_lib.store_The_Doc2Vec(model,_store_path)