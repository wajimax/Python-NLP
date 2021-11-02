# -*- coding: utf-8 -*-
import user_stopword
import unicodedata
import re
import MeCab

#MeCab
mecab = MeCab.Tagger('-Ochasen')

###各フィルターで使用する正規表現のコンパイル###

#PIC
pic_p = re.compile(u"[^\s]+(?=\.(jpg|jpeg|gif|png))\.\2")
#Mail
mail_p = re.compile(u"[\w\d_-]+@[\w\d_-]+\.[\w\d._-]+")
#HTML
html_p = re.compile(u"\<(/?[^\>]+)\>")
#ColorCode
colorcode_p = re.compile(u"'#'?([A-Fa-f0-9]){3}(([A-Fa-f0-9]){3})?")
#URL
url_p = re.compile(u"(?:https?|ftp):\/\/[\w\d/%#$&?()~_.=+-]+")
#symbol
symbol_p = re.compile(u"[!-/:-@[-`{-~]")

#number
number_p = re.compile(u"([0-9]+)")

#english
english_p = re.compile(u"([A-Za-z0-9]+)")

#ひらがな2文字
hiragana_p = re.compile(u"[ぁ-ゞ]{2}")

#カタカナ末尾長音記号
katakan_p = re.compile(u"$ー")

#トークン化
def text_ja(_text,_posType,_formType):
	wordList = []
	
	#改行コードを除去
	text = _text.strip()
	
	#unicode正規化
	CJKText = CJKWidthFilterFactory(_text)
	
	#小文字化
	LCText = LowerCaseFilterFactory(CJKText)
	
	#クレンジング
	RDCText = RegularDataCleansing(LCText)
	
	#トークン化
	mecabTokens = Tokens(RDCText)
	
	#品詞フィルター
	posTokens = JapanesePartOfSpeechStopFilterFactory(mecabTokens,_posType)
	
	#文字数フィルター
	WLTokens = WordLengthFilterFactory(posTokens)
	
	#活用形フィルター + リスト化
	textWords = JapaneseFormFilterFactory(WLTokens,_formType)
	
	#長音記号フィルター
	JKSWords = JapaneseKatakanaStemFilterFactory(textWords)
	
	#アルファベットフィルター
	#nonEnglishWords = englishFilterFactory(JKSWords)
	
	#記号フィルター
	nonSymbolWords = symbolFilterFactory(JKSWords)
	
	#STOP WORDフィルター
	JSWords = JapaneseStopFilterFactory(nonSymbolWords)
	
	#nonNumberWords =  numberFilterFactory(nonSymbolWords)
	nonNumberWords =  numberFilterFactory(JSWords)
	
	#unicode正規化
	#CJKTokens = CJKTokenFilterFactory(JSWords)
	
	return nonNumberWords

#品詞カウント用
def posTagger(_text,_pos_list):
	try:
		wordList = []
		
		#改行コードを除去
		text = _text.strip()
		
		#unicode正規化
		CJKText = CJKWidthFilterFactory(_text)
		
		#小文字化
		LCText = LowerCaseFilterFactory(CJKText)
		
		#クレンジング
		RDCText = RegularDataCleansing(LCText)
		
		#形態素解析
		words = Tokens(RDCText)
		
		#品詞情報のみ取得
		tag_Lists = classifyPos_tag(words,_pos_list)
		
		return tag_Lists
		
	except Exception as e:
		print e

#品詞情報を取得するメソッド
def classifyPos_tag(_words,_pos_list):
	tags = []
	for token in _words.tokens:
		try :
			if token.pos in _pos_list:
				tags.append(token.pos)
		except Exception as e:
			print e
			
	return tags

#pos_detail1カウント用
def detail1Tagger(_text,_detail1_list):
	try:
		wordList = []
		
		#改行コードを除去
		text = _text.strip()
		
		#unicode正規化
		CJKText = CJKWidthFilterFactory(_text)
		
		#小文字化
		LCText = LowerCaseFilterFactory(CJKText)
		
		#クレンジング
		RDCText = RegularDataCleansing(LCText)
		
		#形態素解析
		words = Tokens(RDCText)
		
		#品詞情報のみ取得
		detail1_Lists = detail1_tag(words,_detail1_list)
		
		return detail1_Lists
		
	except Exception as e:
		print e

#pos_detail1を取得するメソッド
def detail1_tag(_words,_detail1_list):
	tags = []
	for token in _words.tokens:
		try :
			if token.pos_detail1 in _detail1_list:
				tags.append(unicode(token.pos_detail1))
				#tags.append(token.pos_detail1)
		except Exception as e:
			print e
			
	return tags


#Subtypeカウント用
def subtypeTagger(_text,_subtype_list):
	try:
		wordList = []
		
		#改行コードを除去
		text = _text.strip()
		
		#unicode正規化
		CJKText = CJKWidthFilterFactory(_text)
		
		#小文字化
		LCText = LowerCaseFilterFactory(CJKText)
		
		#クレンジング
		RDCText = RegularDataCleansing(LCText)
		
		#形態素解析
		words = Tokens(RDCText)
		
		#品詞情報のみ取得
		subtype_Lists = subtype_tag(words,_subtype_list)
		
		return subtype_Lists
		
	except Exception as e:
		print e

#Subtypeを取得するメソッド
def subtype_tag(_words,_subtype_list):
	tags = []
	for token in _words.tokens:
		try :
			if token.pos_detail2 in _subtype_list:
				tags.append(unicode(token.pos_detail2))
				#tags.append(token.pos_detail2)
		except Exception as e:
			print e
			
	return tags

#twitterのアカウントを落とす用
def englishFilterFactory(_tokens):

        nonEnglishTokens = []
        for token in _tokens:
                try :
			if not re.match(english_p,unicode(token,'utf-8')):
				nonEnglishTokens.append(token)
                except Exception as e:
                        print e

        return nonEnglishTokens

#数字を落とす用
def numberFilterFactory(_tokens):
        nonNumberTokens = []
        for token in _tokens:
                try :
                        if not re.match(number_p,unicode(token,'utf-8')):
                                nonNumberTokens.append(token)
                except Exception as e:
                        print e

        return nonNumberTokens

def symbolFilterFactory(_tokens):
	
	nonSymbolTokens = []
	for token in _tokens:
                try :
                        if not re.match(symbol_p,unicode(token,'utf-8')):
                                nonSymbolTokens.append(token)
                except Exception as e:
                        print e

	return nonSymbolTokens

#unicode正規化
def CJKTokenFilterFactory(_tokens):
	CJKTokens = []
	for token in _tokens:
                try :
                	unicode_token = unicode(token)
			nfkc_token = unicodedata.normalize('NFKC', unicode_token)
			CJKToken = nfkc_token.encode('utf-8')
			CJKTokens.append(CJKToken)
		except Exception as e:
                        print e
        return CJKTokens

#Unicode正規化
def CJKWidthFilterFactory(_text):
	#改行コードの除去
	#text = _text.rstrip()
	
	try :
		#Unicode正規化
		unicode_text = unicode(_text)
		nfkc_text = unicodedata.normalize('NFKC', unicode_text)
		CJKText = nfkc_text.encode('utf-8')
	except Exception as e:
		CJKText = ""
		print e
		
	return CJKText

#英数字の小文字化
def LowerCaseFilterFactory(_CJKText):
	LCText = _CJKText.lower()
	return LCText

#正規表現によるクレンジング
def RegularDataCleansing(_LCText):
	
	#unicodeにデコード
	LCText = _LCText.decode('utf-8')
	
	#URL
	s_result = url_p.search(LCText)
	urlText = LCText
	while s_result is not None:
		urlText = urlText.replace(s_result.group(0),u" ")
		#print s_result.group(0)
		s_result = url_p.search(urlText)
	
	#PIC
	s_result = pic_p.search(urlText)
	picText = urlText
        while s_result is not None:
                picText = picText.replace(s_result.group(0),u" ")
		s_result = url_p.search(picText)
		
	#Mail
	s_result = mail_p.search(picText)
        mailText = picText
	while s_result is not None:
                mailText = mailText.replace(s_result.group(0),u" ")
		#print s_result.group(0)
		s_result = mail_p.search(mailText)
	
	#html
	s_result = html_p.search(mailText)
        htmlText = mailText
	while s_result is not None:
                htmlText = mailText.replace(s_result.group(0),u" ")
		#print s_result.group(0)
		s_result = mail_p.search(htmlText)
			
	#COLOR CODE
	s_result = colorcode_p.search(htmlText)
	colorcodeText = htmlText
        while s_result is not None:
                colorcodeText = htmlText.replace(s_result.group(0),u" ")
		s_result = colorcode_p.search(colorcodeText)
	
	#記号
	s_result = symbol_p.search(colorcodeText)
	symbolText = colorcodeText
        while s_result is not None:
                symbolText = colorcodeText.replace(s_result.group(0),u" ")
		s_result = colorcode_p.search(symbolText)
	
	
	#数字
	s_result = number_p.search(symbolText)
	numberText = symbolText
        while s_result is not None:
                numberText = symbolText.replace(s_result.group(0),u" ")
		#print s_result.group(0)
		s_result = colorcode_p.search(numberText)
	
	#utf-8にエンコード	
	RDText = mailText.encode('utf-8')
	return RDText
	
#MeCabで単語をToken化
def mecabTokenizer(_text):
        mecabTokens = Tokens(_text)
        return mecabTokens

#品詞フィルタ
def JapanesePartOfSpeechStopFilterFactory(_mecabTokens,_posType):
	posTokens = []
	#単語ごとにFor
	for mecabToken in _mecabTokens.tokens:
		#品詞が指定されたリストに含まれる場合
		if mecabToken.pos in _posType:
			#要素をリストに追加
			posTokens.append(mecabToken)
	return posTokens

#文字数での除去(1文字除去、ひらがな2文字除去)
def WordLengthFilterFactory(_posTokens):
	WLTokens = []
	for token in _posTokens:
		try :
			#1文字単語を除去
			if len(unicode(token.surface,'utf-8')) == 1:continue
			elif len(unicode(token.surface,'utf-8')) == 2:
				#ひらがな2文字は除去
				if re.match(hiragana_p,unicode(token.surface,'utf-8')):
					continue
				else:
					WLTokens.append(token)
			else:
				WLTokens.append(token)
		except Exception as e:
			print e	
	return WLTokens

#活用形のフィルタ
def JapaneseFormFilterFactory(_WLTokens,_formType):
	textWords = []
	for token in _WLTokens:
		try:
			if _formType == "basic":
				if token.basic == "*":
					textWords.append(token.surface)
				else:
					textWords.append(token.basic)
			else:
				JFTokens.surface(token.surface)
		except Exception as e:
			print e
	return textWords

#末尾の長音記号を除去
def JapaneseKatakanaStemFilterFactory(_textWords):
		JKSWords = []
		for word in _textWords:
			try:
				re.sub(katakan_p,unicode(word,'utf-8'),"")
				JKSWords.append(word)
			except Exception as e:
				print e
		return JKSWords
		
#STOP WORDフィルタ
def JapaneseStopFilterFactory(_JKSWords):
	JSWords = []
	for word in _JKSWords:
		try:
			if unicode(word,'utf-8') in user_stopword.User_stopword.user_stop_utf:
				continue
			else:
				#print word
				JSWords.append(word)
		except Exception as e:
				print e
	return JSWords


class Tokens(object) :
        # text の形態素情報を保持する
        def __init__ (self,_text):
                self.text = _text
                node = mecab.parseToNode(_text)
                self.tokens = []
                while node:
                        self.tokens.append(Token(node.surface,*node.feature.split(',')))
                        node = node.next

class Token(object):
        # 形態素の情報
        def __init__(self,_surface,*_args):
                #Mecab Format
                #表層形/t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
                self.surface = _surface #表層情報

                try:
                        self.pos = _args[0] # 品詞
                        self.pos_detail1 = _args[1] #品詞分類1
                        self.pos_detail2 = _args[2] #品詞分類2
                        self.pos_detail3 = _args[3] #品詞分類3
                        self.verb_form = _args[4] #活用形
                        self.verb_type = _args[5] #活用型
                        self.basic = _args[6] #原型
                        self.reading = _args[7] #読み
                        self.pronunciation = _args[8] #発音
                        self.type = True #すべての要素が格納できた時のFlg
                except IndexError:
                        self.type = False #すべての要素が格納できなかった時のFlg
