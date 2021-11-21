from gensim.models import Word2Vec, word2vec

# 加载语料
corpus = word2vec.LineSentence("/Users/xuhaoshuai/GitHub/HumanIE_IPM/src/softmatch/word2vec_traning_text_clean.txt")
# 每一行是一个句子，分好词，并且以空格分开，不去除任何停用词。

# 训练语料
model =Word2Vec(
    sentences=corpus, # 语料库
    min_count=1, # < 1 的被舍弃掉
    sg=1, # 使用的训练方法。1 是 skip-gram。0 是 CBOW。小语料用 skip-gram 即可。
    )    
model.save('/Users/xuhaoshuai/GitHub/HumanIE_IPM/src/softmatch/word2vec.model')
