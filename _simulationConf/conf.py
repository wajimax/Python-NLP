# -*- coding: utf-8 -*-


##TOPIC�p�̕ϐ��i�[�N���X##
class simulation_conf(object):
	
	#������
	simulation_Name = "jsik_stackoverflow"
	
	#�I���W�i���t�@�C��
	fileName = "stackoverflow_file_body_regex_extract_NFKC.txt"
	
	#�킩�������t�@�C��
	wakachi_fileName = fileName + "_wakachi"
	
	#�I���W�i���t�@�C���̃p�X
	original_fileName_path = "../_input/" + fileName
	
	#�킩�������t�@�C���̃p�X
	wakachi_fileName_path = "../_output/wakachi/" + wakachi_fileName
	
	#�����̕ۑ��p�X
	gensim_dic_path = "../_output/corpus/" + wakachi_fileName + "_gensimdic"
	
	#�R�[�p�X�̕ۑ��p�X
	gensim_corpa_path = "../_output/corpus/" + wakachi_fileName + "_gensimcorpa"
	
	#�g�s�b�N��
	topicNum = 300
	
	#LSI�̎���(300-500�������l)
	#http://dl.acm.org/citation.cfm?id=1458105
	lsi_k = 300
	
	#LDA�P�ꕪ�z�̕ۑ��p
	lda_gensim_topic_words = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_words.txt"
	
	#LDA�����m���̕ۑ��p
	lda_gensim_topic_probability = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_probability.txt"
	
	#LDA���f���̕ۑ��p
	lda_gensim_topic_model = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_model"
	
	#LDA���f���̕����ւ̊����m���̕ۑ��p
	lda_gensim_topic_allot = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_topic_allot"
	
	#LDA���f���̕����ւ̍ő劄���g�s�b�N�̕ۑ��p
	lda_gensim_topic_max_allot = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_topic_max_allot"
	
	
	#LSI�P�ꕪ�z�̕ۑ��p
	lsi_gensim_topic_words = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_words.txt"
	
	#LSI�����m���̕ۑ��p
	lsi_gensim_topic_probability = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_probability.txt"
	
	#LSI���f���̕ۑ��p
	lsi_gensim_topic_model = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_model"
	
	#LSI���f���̕����ւ̊����m���̕ۑ��p
	lsi_gensim_topic_allot = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_topic_allot"
	
	#LSI���f���̕����ւ̍ő劄���g�s�b�N�̕ۑ��p
	lsi_gensim_topic_max_allot = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_topic_max_allot"
	
	
	#HDP�P�ꕪ�z�̕ۑ��p
	hdp_gensim_topic_words = "../_output/topic/hdp_topic_" + wakachi_fileName + "_words.txt"
	
	#HDP�����m���̕ۑ��p
	hdp_gensim_topic_probability = "../_output/topic/hdp_topic_" + wakachi_fileName + "_probability.txt"
	
	#HDP���f���̕ۑ��p
	hdp_gensim_topic_model = "../_output/topic/hdp_topic_" + wakachi_fileName + "_model"
	
	#HDP���f���̕����ւ̊����m���̕ۑ��p
	hdp_gensim_topic_allot = "../_output/topic/hdp_topic_" + wakachi_fileName + "_topic_allot"
	
	#HDP���f���̕����ւ̍ő劄���g�s�b�N�̕ۑ��p
	hdp_gensim_topic_max_allot = "../_output/topic/hdp_topic_" + wakachi_fileName + "_topic_max_allot"
	
	
##�����v�Z�p�̕ϐ��i�[�N���X##
class similarity_conf(object):
	
	#������
	simulation_Name = "apple"
	
	#�I���W�i���t�@�C��
	fileName = "apple_support.txt"
	
	#�����v�Z�p�̃t�@�C����
	analyze_file = "apple_support.txt"
	
	#�킩�������t�@�C��(�R�[�p�X�S��)
	wakachi_fileName = fileName + "_wakachi"
	
	#�킩�������t�@�C��(�����v�Z�t�@�C��)
	wakachi_analyze = analyze_file + "_wakachi"
	
	#�����������̃t�@�C���̃p�X
	wakachi_fileName_path = "../_output/wakachi/" + wakachi_fileName
	
	#�I���W�i���t�@�C���̃p�X
	original_fileName_path = "../_input/" + fileName
	
	#�����v�Z�p�̃t�@�C����
	analyze_file_path = "../_output/wakachi/" + wakachi_analyze
	
	#LSI�t�@�C���̃p�X
	lsi_corpa_path = "../_output/corpus/lsi_model_" + wakachi_fileName + "_gensimcorpa"
	
	#LSI�����v�Z�t�@�C���̏o�̓p�X
	similarity_file_path = "../_output/similarity/lsi_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#word2vec�̏o�͒P�ꐔ
	word2vec_similarity_words_num = 10
	
	#word2vec�̗ގ��x���ʏo�̓p�X
	word2vec_similarity_path = "../_output/similarity/word2vec_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#word2vec���f���ۑ��p�̃p�X
	word2vec_model_path = "../_output/corpus/word2vec_model_" + wakachi_fileName + "_gensimcorpa"
	
	#doc2vec�̗ގ��x���ʏo�̓p�X
	doc2vec_similarity_path = "../_output/similarity/word2vec_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#doc2vec���f���ۑ��p�̃p�X
	doc2vec_model_path = "../_output/corpus/word2vec_model_" + wakachi_fileName + "_gensimcorpa"
