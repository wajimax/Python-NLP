# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#ファイル名
	fileName = conf.simulation_conf.wakachi_fileName
	
	#Inputファイルパス
	input_filePath = "../_output/wakachi/"
	
	#Outputファイルパス
	output_filePath = "../_output/corpus/"
	
	#辞書・コーパス作成
	topic.topic_corpus_maker(fileName,input_filePath,output_filePath)
	
	print "Finished"