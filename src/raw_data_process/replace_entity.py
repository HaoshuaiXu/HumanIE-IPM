from os import sep
import pandas as pd


sent_set = pd.read_csv(
    "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set/teacher.csv",
    sep=','
)

replaced_sent_list = []
for index, row in sent_set.iterrows():
    replaced_sent = row['sent'].replace(row['entity1'], "人物一").replace(row['entity2'], "人物二")
    replaced_sent_list.append(replaced_sent)

# 如果日后需要保留 sent id，可以改造这里。目前来说没有需要，因此我就省了这一步。
# replaced_sent_set = pd.DataFrame(replaced_sent_list, columns=['replaced_set'])
with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set_replace-entity/teacher.csv", 'w') as f:
    for l in replaced_sent_list:
        f.writelines(l + '\n')
