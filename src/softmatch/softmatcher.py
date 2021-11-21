from gensim.models import Word2Vec, word2vec
from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np

# def get_cos_similar(v1: list, v2: list):
#     num = float(np.dot(v1, v2))  # 向量点乘
#     denom = np.linalg.norm(v1) * np.linalg.norm(v2)  # 求模长的乘积
#     return 0.5 + 0.5 * (num / denom) if denom != 0 else 0

if __name__ == '__main__':
    # 关系和迭代次数
    relation_name = 'brother'
    iteractive_num = '1'


    # 数据准备
    rule_set = pd.read_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/labeled_rule/" + relation_name + "/" + iteractive_num + ".csv",
        header=0,index_col='id'
    )
    neg_rule_set = rule_set[rule_set['label'] == 0]
    pos_rule_set = rule_set[rule_set['label'] == 1]

    sent_set = pd.read_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/sent_test/" + relation_name + ".csv",
        names=['sent']
        )
    sent_set['softmatch_score'] = 'NaN' # 新增一列，记录匹配分数
    sent_set['softmatch'] = 'NaN' # 新增一列，记录软匹配标签


    # 加载 Word2Vec 模型
    model = Word2Vec.load("/Users/xuhaoshuai/GitHub/HumanIE_IPM/src/softmatch/word2vec.model")


    # 计算负规则和句子软匹配相似度
    for sent_index, sent_row in sent_set.iterrows():
        sennt_list = sent_row['sent'].split()
        for rule_index, rule_row in neg_rule_set.iterrows():
            rule_list = rule_row['rule'].split()
            softmatch_score = model.wv.n_similarity(sennt_list, rule_list)
            sent_row['softmatch_score'] = softmatch_score
            if softmatch_score >= 0.9:
                # print(softmatch_score)
                sent_row['softmatch'] = 0
                break
    
    neg_sent_set = sent_set[sent_set['softmatch'] == 0]
    neg_sent_set.to_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/softmatch/" + relation_name + "/neg/" + iteractive_num + ".csv",
        index_label='id'
    )


    # 计算正规则和句子软匹配相似度
    left_sent_set = sent_set[sent_set['softmatch'] == 'NaN']
    # print(left_sent_set)

    for sent_index, sent_row in left_sent_set.iterrows():
        sennt_list = sent_row['sent'].split()
        for rule_index, rule_row in pos_rule_set.iterrows():
            rule_list = rule_row['rule'].split()
            softmatch_score = model.wv.n_similarity(sennt_list, rule_list)
            sent_row['softmatch_score'] = softmatch_score
            if softmatch_score >= 0.8:
                print(softmatch_score)
                sent_row['softmatch'] = 1
                break
    
    pos_sent_set = left_sent_set[left_sent_set['softmatch'] == 1]
    pos_sent_set.to_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/softmatch/" + relation_name + "/pos/" + iteractive_num + ".csv",
        index_label='id'
    )


    # 没被匹配上的句子
    non_sent_set = left_sent_set[left_sent_set['softmatch'] == 'NaN']
    non_sent_set.to_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/softmatch/" + relation_name + "/non/" + iteractive_num + ".csv",
        index_label='id'
    )
