# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import similarity
import conf
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == "__main__":
	print "Start"
	
	#word2vec���f���̕ۑ��p�p�X
	word2vec_model_path = make_dictionary_conf.similarity_conf.word2vec_model_path
	
	#���͗p�̃p�X
	word2vec_analyze_file_path = make_dictionary_conf.similarity_conf.analyze_file_path
	
	#�ގ��x�̏o�͒P�ꐔ
	word2vec_similarity_words_num = make_dictionary_conf.similarity_conf.word2vec_similarity_words_num
	
	#���ʂ�ۑ�����p�X
	word2vec_similarity_path = make_dictionary_conf.similarity_conf.word2vec_similarity_path
	
	#word2vec���f�����쐬
	similarity.word2vec_similar_calculation(word2vec_model_path,word2vec_analyze_file_path,word2vec_similarity_words_num,word2vec_similarity_path)
	
	print "Finished"