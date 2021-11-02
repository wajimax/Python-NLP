# Python-NLP

## 使用ライブラリ
・gensim
https://radimrehurek.com/gensim/index.html

・MeCab: Yet Another Part-of-Speech and Morphological Analyzer
https://taku910.github.io/mecab/

## 概要説明
_input
→ 解析対象のファイルを格納するディレクトリ

_library
→ ライブラリを呼び出すプログラムが格納されたディレクトリ
・gensim_lib.py
→ gensimのメソッドを呼び出すためのプログラム

・mecab_lib.py
→ MeCabのメソッドを呼び出すためのプログラム

・user_stopword.py
→ HTMLタグを除去するためのストップワード用のプログラム

_output
→ 解析結果を格納するディレクトリ
	corpus
	→ トピックに関するファイルが格納されるディレクトリ
	
	similarity
	→ gensimのコーパスが格納されるディレクトリ
	
	topic
	→ トピックに関するファイルが格納されるディレクトリ
		トピックの単語分布:*_words.txt
		単語分布の生成確率 : *probability.txt
		文書に対する割当確率 : *_topic_allot
		文書に対して最も生成確率が高かったTOPIC :*_topic_max_allot
	
	wakachi
	→ 形態素解析後の 分かち書きファイルを格納するディレクトリ

_simulationConf
実験を行う際には「corpus」「topic」「wakachi」「allot」の
4ディレクトリに対して、conf.pyの"simulation_Name"で指定した
ディレクトリ名と同じフォルダを作成してから実験すること

analyze
→ 特定のファイルからわかち書きを生成するプログラムが格納されたディレクトリ
	・data_analyze.py
	→ 分かち書きプログラム
	
	・make_analyzedata.py
	→ 実行プログラム
	
similarity
→ 類似度を計算するプログラム
	・similarity.py
	→ 共通メソッドが格納されたプログラム
	
	・lsi_similarity.py
	→ LSIモデルによる距離計算とファイル出力
	
	・word2vec_make_model.py
	→ word2vecモデルの生成
	
	・word2vec_similarity.py
	→ word2vecによる特定の単語に対する類似度上位の単語を生成
	
topic

	・topic.py
	→  共通メソッドが格納されたプログラム
	
	・make_gensim_files.py
	→ 「分かち書きファイル」を「gensim」のコーパスに変換するプログラム
	
	・hdp_topic_allot.py
	→ HDPモデルをによるトピック割当を実施するプログラム
	
	・hdp_topic_extract.py
	→ HDPモデルをによるトピック抽出を実施するプログラム
	
	・lda_topic_allot.py
	→ LDAモデルをによるトピック割当を実施するプログラム
	
	・lda_topic_extract.py
	→ LDAモデルをによるトピック抽出を実施するプログラム
	
	・lsi_topic_allot.py
	→ LSIモデルをによるトピック割当を実施するプログラム
	
	・lsi_topic_extract.py
	→ LSIモデルをによるトピック抽出を実施するプログラム
