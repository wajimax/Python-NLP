# -*- coding: utf-8 -*-
import sys
sys.path.append('../_library')
sys.path.append('../_simulationConf')
import gensim_lib
import topic
import conf

if __name__ == "__main__":
	print "Start"
	
	#�t�@�C����
	fileName = conf.simulation_conf.wakachi_fileName
	
	#Input�t�@�C���p�X
	input_filePath = "../_output/wakachi/"
	
	#Output�t�@�C���p�X
	output_filePath = "../_output/corpus/"
	
	#�����E�R�[�p�X�쐬
	topic.topic_corpus_maker(fileName,input_filePath,output_filePath)
	
	print "Finished"