from prefixspan import PrefixSpan
import pandas as pd

# with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/sent_train/brother.csv", "r") as f:
#     db = [i.strip('\n') for i in f.readlines()]
#     print(db)

relation = 'teacher'
iterative_num = '1'

sent_set = pd.read_csv(
    "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/sent_train/" + relation +".csv",
    header=0
    )

db = []
for s in sent_set['sent']:
    db.append(s.split())

# 这段代码是在用 PrefixSpan 进行挖掘
ps = PrefixSpan(db)
ps.minlen = 3
ps.maxlen = 6   
rules = ps.topk(200) # [(1, ['a', 'b', 'c']), (2, ['a', 'b'])]

# 这段代码是将挖掘结果的格式转换一下
i = 0
while i < len(rules):
    rules[i] = list(rules[i])
    tmp = ''
    for w in rules[i][1]:
        tmp = tmp + w + ' '
    rules[i][1] = tmp.rstrip(' ')
    i = i + 1
 
# 这段代码是将挖掘结果通过 pandas 来写入硬盘
rules_set = pd.DataFrame(rules, columns=['frequency', 'rule'])
rules_set.to_csv(
    "/Users/xuhaoshuai/GitHub/HumanIE_IPM/rule/" + relation +"/" + iterative_num + ".csv",
    index_label='id',
    columns=['rule', 'frequency']
)