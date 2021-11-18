import re
from zhon.hanzi import punctuation
import string

relation_name = 'teacher'

with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set_replace-entity/" + relation_name + ".csv", "r") as f:
    sent = [x.strip('\n') for x in f.readlines()]

with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/cn_stopwords.txt", 'r') as f:
    stpws = [x.strip('\n') for x in f.readlines()]

# 去除停用词
sent_clean = []
stpws.append('')
stpws.append('')
for s in sent:
    s = re.sub('[\d]', '', s) # 去除数字
    s = re.sub('[a-zA-Z]', '', s) # 去除英文字母
    for cn_punc in punctuation: # 去除中文标点
        s = s.replace(cn_punc, '')
    for en_punc in string.punctuation: # 去除英文标点
        s = s.replace(en_punc, '')
    s = [w for w in s.split(' ') if w not in stpws] # 去除停用词
    sent_clean.append(s)

with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set_remove-stopwords/" + relation_name + ".csv", 'w+') as f:
    for s in sent_clean:
        tmp = ''
        for w in s:
            tmp = tmp + ' ' + w # 这句逻辑有个问题，就是会让第一个字符前面也有空格，注意一下
        f.writelines(tmp + '\n')