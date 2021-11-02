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
	
	#word2vecモデルの保存用パス
	word2vec_model_path = make_dictionary_conf.similarity_conf.word2vec_model_path
	
	#分析用のパス
	word2vec_analyze_file_path = make_dictionary_conf.similarity_conf.analyze_file_path
	
	#類似度の出力単語数
	word2vec_similarity_words_num = make_dictionary_conf.similarity_conf.word2vec_similarity_words_num
	
	#結果を保存するパス
	word2vec_similarity_path = make_dictionary_conf.similarity_conf.word2vec_similarity_path
	
	#word2vecモデルを作成
	similarity.word2vec_similar_calculation(word2vec_model_path,word2vec_analyze_file_path,word2vec_similarity_words_num,word2vec_similarity_path)
	
	print "Finished"