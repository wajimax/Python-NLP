# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import similarity
import make_dictionary_conf
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == "__main__":
	print "Start"
	
	#word2vecモデルに変換する分かち書きのファイルパス
	wakachi_path = make_dictionary_conf.similarity_conf.wakachi_fileName_path
	
	#word2vecモデルの保存用パス
	store_path = make_dictionary_conf.similarity_conf.word2vec_model_path
	
	#word2vecモデルを作成
	similarity.word2vec_model_maker(wakachi_path,store_path)
	
	print "Finished"