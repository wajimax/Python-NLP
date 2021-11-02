# -*- coding: utf-8 -*-


##TOPIC用の変数格納クラス##
class simulation_conf(object):
	
	#実験名
	simulation_Name = "jsik_stackoverflow"
	
	#オリジナルファイル
	fileName = "stackoverflow_file_body_regex_extract_NFKC.txt"
	
	#わかち書きファイル
	wakachi_fileName = fileName + "_wakachi"
	
	#オリジナルファイルのパス
	original_fileName_path = "../_input/" + fileName
	
	#わかち書きファイルのパス
	wakachi_fileName_path = "../_output/wakachi/" + wakachi_fileName
	
	#辞書の保存パス
	gensim_dic_path = "../_output/corpus/" + wakachi_fileName + "_gensimdic"
	
	#コーパスの保存パス
	gensim_corpa_path = "../_output/corpus/" + wakachi_fileName + "_gensimcorpa"
	
	#トピック数
	topicNum = 300
	
	#LSIの次元(300-500が推奨値)
	#http://dl.acm.org/citation.cfm?id=1458105
	lsi_k = 300
	
	#LDA単語分布の保存用
	lda_gensim_topic_words = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_words.txt"
	
	#LDA生成確率の保存用
	lda_gensim_topic_probability = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_probability.txt"
	
	#LDAモデルの保存用
	lda_gensim_topic_model = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_model"
	
	#LDAモデルの文書への割当確率の保存用
	lda_gensim_topic_allot = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_topic_allot"
	
	#LDAモデルの文書への最大割当トピックの保存用
	lda_gensim_topic_max_allot = "../_output/topic/lda_topic_" + wakachi_fileName + "_" + str(topicNum) + "_topic_max_allot"
	
	
	#LSI単語分布の保存用
	lsi_gensim_topic_words = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_words.txt"
	
	#LSI生成確率の保存用
	lsi_gensim_topic_probability = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_probability.txt"
	
	#LSIモデルの保存用
	lsi_gensim_topic_model = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_model"
	
	#LSIモデルの文書への割当確率の保存用
	lsi_gensim_topic_allot = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_topic_allot"
	
	#LSIモデルの文書への最大割当トピックの保存用
	lsi_gensim_topic_max_allot = "../_output/topic/lsi_topic_" + wakachi_fileName + "_" + str(lsi_k) + "_topic_max_allot"
	
	
	#HDP単語分布の保存用
	hdp_gensim_topic_words = "../_output/topic/hdp_topic_" + wakachi_fileName + "_words.txt"
	
	#HDP生成確率の保存用
	hdp_gensim_topic_probability = "../_output/topic/hdp_topic_" + wakachi_fileName + "_probability.txt"
	
	#HDPモデルの保存用
	hdp_gensim_topic_model = "../_output/topic/hdp_topic_" + wakachi_fileName + "_model"
	
	#HDPモデルの文書への割当確率の保存用
	hdp_gensim_topic_allot = "../_output/topic/hdp_topic_" + wakachi_fileName + "_topic_allot"
	
	#HDPモデルの文書への最大割当トピックの保存用
	hdp_gensim_topic_max_allot = "../_output/topic/hdp_topic_" + wakachi_fileName + "_topic_max_allot"
	
	
##距離計算用の変数格納クラス##
class similarity_conf(object):
	
	#実験名
	simulation_Name = "apple"
	
	#オリジナルファイル
	fileName = "apple_support.txt"
	
	#距離計算用のファイル名
	analyze_file = "apple_support.txt"
	
	#わかち書きファイル(コーパス全体)
	wakachi_fileName = fileName + "_wakachi"
	
	#わかち書きファイル(距離計算ファイル)
	wakachi_analyze = analyze_file + "_wakachi"
	
	#分かち書きのファイルのパス
	wakachi_fileName_path = "../_output/wakachi/" + wakachi_fileName
	
	#オリジナルファイルのパス
	original_fileName_path = "../_input/" + fileName
	
	#距離計算用のファイル名
	analyze_file_path = "../_output/wakachi/" + wakachi_analyze
	
	#LSIファイルのパス
	lsi_corpa_path = "../_output/corpus/lsi_model_" + wakachi_fileName + "_gensimcorpa"
	
	#LSI距離計算ファイルの出力パス
	similarity_file_path = "../_output/similarity/lsi_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#word2vecの出力単語数
	word2vec_similarity_words_num = 10
	
	#word2vecの類似度結果出力パス
	word2vec_similarity_path = "../_output/similarity/word2vec_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#word2vecモデル保存用のパス
	word2vec_model_path = "../_output/corpus/word2vec_model_" + wakachi_fileName + "_gensimcorpa"
	
	#doc2vecの類似度結果出力パス
	doc2vec_similarity_path = "../_output/similarity/word2vec_" + wakachi_fileName + "_" + wakachi_analyze + "_similarity"
	
	#doc2vecモデル保存用のパス
	doc2vec_model_path = "../_output/corpus/word2vec_model_" + wakachi_fileName + "_gensimcorpa"
