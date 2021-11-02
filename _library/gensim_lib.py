# -*- coding: utf-8 -*-

import gensim
from gensim import corpora, models, similarities
from gensim.models import doc2vec

######    コーパス・辞書    ######
##トークンからGensimの辞書を作成##
def tokens_To_GensimDic(_tokens):
	dictionary = corpora.Dictionary(_tokens)
	return dictionary

##トークンからGensimのコーパスを作成##
def tokens_To_GensimCorpus(_tokens,_dictionary):
	corpus = [_dictionary.doc2bow(document) for document in _tokens]
	return corpus

##Gensimの辞書を指定ディレクトリに保存##
def store_The_GensimDic(_dictionary,_path):
	_dictionary.save(_path)

##Gensimの辞書を指定ディレクトリから読込##
def load_The_GensimDic(_path):
	dictionary = gensim.corpora.dictionary.Dictionary.load(_path)
	return dictionary

##Gensimのコーパスを指定ディレクトリに保存##
def store_The_GensimCorpus(_corpus,_path):
	corpora.MmCorpus.serialize(_path,_corpus)

##Gensimのコーパスを指定ディレクトリから読込##
def load_The_GensimCorpus(_path):
	corpus = gensim.corpora.MmCorpus(_path)
	return corpus

##GensimのコーパスをTFIDFモデルを構築##
def gensimCorpus_To_TfidfInstance(_corpus):
	tfidf_instance=models.TfidfModel(_corpus)
	return tfidf_instance

##GensimのコーパスをTFIDFモデルのコーパスに変換##
def gensimCorpus_To_TfidfCorpus(_corpus,_tfidf_instance):
	tfidf_corpus = _tfidf_instance[_corpus]
	return tfidf_corpus

######    LDA    ######
##LDAトピックの抽出##
def extraction_LdaTopic(_dictionary,_corpus,_num_topics):
	lda_Topic = gensim.models.ldamodel.LdaModel(corpus=_corpus, num_topics=_num_topics, id2word=_dictionary)
	return lda_Topic

##LDAトピックの保存##
def store_The_LdaTopic(_lda_Topic,_path):
	_lda_Topic.save(_path)

##LDAトピックの読込##
def load_The_LdaTopic(_path):
	lda_Topic = gensim.models.LdaModel.load(_path)
	return lda_Topic

##LDAトピックの割当##
def doc_to_ldatopic_distribution(_text,_ldatopic):
	doc_lda = _ldatopic[_text]
	return doc_lda


######    LSI    ######
##LSIトピックの抽出##
def extraction_LsiTopic(_dictionary,_tfidf_corpus,_num_topics):
	lsi_Topic = models.LsiModel(_tfidf_corpus, id2word=_dictionary, num_topics=_num_topics)
	return lsi_Topic

##LSIトピックの保存##
def store_The_LsiTopic(_lsi_Topic,_path):
	_lsi_Topic.save(_path)

##LSIトピックの読込##
def load_The_LsiTopic(_path):
	lsi_Topic = gensim.models.LsiModel.load(_path)
	return lsi_Topic

##LSIトピックの割当##
def doc_to_lsitopic_distribution(_text,_lsitopic):
	doc_lsi = _lsitopic[_text]
	return doc_lsi

######    HDP    ######
##HDPトピックの抽出##
def extraction_HdpTopic(_dictionary,_corpus):
	hdp_Topic = models.HdpModel(_corpus, id2word=_dictionary)
	return hdp_Topic

##HDPトピックの保存##
def store_The_HdpTopic(_hdp_Topic,_path):
	_hdp_Topic.save(_path)

##HDPトピックの読込##
def load_The_HdpTopic(_path):
	hdp_Topic = gensim.models.HdpModel.load(_path)
	return hdp_Topic

##HDPトピックの割当##
def doc_to_hdptopic_distribution(_text,_hdptopic):
	doc_hdp = _hdptopic[_text]
	return doc_hdp

######    LSIにおける類似度    ######
##入力クエリをLSIのベクトル空間に変換##
def lsi_convert_queries(_dictionary,_lsi_Topic,_text):
	vec_bow = _dictionary.doc2bow(_text.split())
	vec_lsi = _lsi_Topic[vec_bow]
	return vec_lsi
	
##コーパスをLSIのベクトル空間に変換##
def lsi_convert_corpus(_corpus,_lsi_Topic):
	index = similarities.MatrixSimilarity(_lsi_Topic[_corpus])
	return index
	
##LSIのベクトル空間を保存##
def store_The_lsi_corpus(_index,_path):
	_index.save(_path)
	
##LSIのベクトル空間を読込##
def load_The_lsi_corpus(_path):
	index = similarities.MatrixSimilarity.load(_path)
	return index
	
##コーパスと入力クエリとのLSIのベクトル空間上の類似度を算出##
def lsi_similarity_calculation(_vec_lsi,_index):
	sims = _index[_vec_lsi]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
	
######    Word2Vec    ######
##Word2Vecインスタンス作成##
def tokens_To_Word2Vec(_wakachi_path):
	
	#分かち書き済みのテキストファイルを読込
	sentences = models.word2vec.LineSentence(_wakachi_path)
	
	#Word2Vecのインスタンス作成
	model = models.word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
	
	return model
	
##Word2Vecモデルの保存##
def store_The_Word2Vec(_model,_path):
	_model.save(_path)
	
##Word2Vecモデルの読込##
def load_The_Word2Vec(_path):
	model = models.word2vec.Word2Vec.load(_path)
	return model

##特定の単語に対する類似度上位Nの単語を返却##
def word_To_Word2Vec_list(_word,_model,_wordNum):
	
	try:
		result = _model.most_similar(unicode(_word, 'utf-8'))
		#result = _model.most_similar(positive=_word,topn=_wordNum)
		
	except KeyError:
		#print "## not in vocabulary(under min_count) ##"
		result = ["\t\t","\t\t"]
		
	return result

######    Doc2Vec    ######
##Doc2Vecインスタンス作成##
def tokens_To_Doc2Vec(_wakachi_path):
	
	print _wakachi_path
	
	#分かち書き済みのテキストファイルを読込
	sentences = models.doc2vec.TaggedLineDocument(_wakachi_path)
	
	#Word2Vecのインスタンス作成
	model = models.doc2vec.Doc2Vec(sentences, size=300, min_count=20, window=15)
	
	return model
	
##Doc2Vecモデルの保存##
def store_The_Doc2Vec(_model,_path):
	model.save(_path)
	
##Doc2Vecモデルの読込##
def load_The_Doc2Vec(_path):
	model = models.doc2vec.Doc2Vec.load(_path)
	return model

##ある文書と類似度が近い文書群を返却##
def doc2Vec_similar_list(_doc,_model,_docsNum):
	result = _model.docvecs.most_similar(_doc,topn=_docsNum)
	return result

##2つの文書の類似度を算出##
def doc2Vec_similarity_calculation(_doc1,_doc2,_model):
	result = _model.docvecs.similarity(_doc1,_doc2)
	return result