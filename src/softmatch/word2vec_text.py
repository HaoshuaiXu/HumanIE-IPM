# 该文件是用来准备 word2vec 模型训练的文本的
import re
from zhon.hanzi import punctuation
import string


if __name__ == '__main__':
    # 读取语料库文件
    with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/src/softmatch/word2vec_traning_text.txt", 'r') as f:
        corpus = [x.strip('\n') for x in f.readlines()]
    
    # 去除不需要的字符
    clean_corpus = []
    for c in corpus:
        c = re.sub('[\d]', '', c) # 去除数字
        c = re.sub('[a-zA-Z]', '', c) # 去除英文字母
        for cn_punc in punctuation: # 去除中文标点
            c = c.replace(cn_punc, '')
        for en_punc in string.punctuation: # 去除英文标点
            c = c.replace(en_punc, '')
        clean_corpus.append(c)
    
    # 写入干净的语料库文件
    with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/src/softmatch/word2vec_traning_text_clean.txt", 'w') as f:
        for c in clean_corpus:
            f.writelines(c + '\n')