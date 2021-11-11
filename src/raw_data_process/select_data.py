import pandas as pd

sent_relation = pd.read_csv("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/rawdata/open_data(all)/sent_relation_train.txt", sep='\t', names=['sent_id', 'relation_id'])
friend_sent_id = sent_relation[sent_relation['relation_id'] == '30']['sent_id'] # 30被识别为了字符串类型
print(friend_sent_id)