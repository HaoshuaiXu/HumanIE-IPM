# HumanIE_IPM

## 文件夹结构

```tree
.
├── README.md
├── data: 放置未经处理过的原始数据以及经过预处理的数据的文件夹
│   ├── README.md
│   ├── backup: 备份文件夹
│   ├── cn_stopwords.txt: 停用词
│   ├── opendata_sent_id: 句子 id
│   ├── opendata_sent_set: 句子集
│   ├── opendata_sent_set_remove-stopwords: 去除停用词、替换了实体的句子集
│   ├── opendata_sent_set_replace-entity: 未去除停用词、但替换了实体的句子集
│   ├── raw_data: 原始数据文件夹
│   ├── sent_test: 测试集，用于迭代挖掘规则和匹配
│   ├── sent_train: 训练集，用于挖掘种子规则
│   └── sent_veri: 验证集，用于计算规则的各项指标
├── hard_match
│   ├── neg
│   ├── none
│   └── pos
├── labeled_rule
│   ├── brother
│   ├── couple
│   ├── friend
│   ├── parentschild
│   └── teacher
├── rule
│   ├── brother
│   ├── couple
│   ├── friend
│   ├── parentschild
│   └── teacher
├── rule.zip
├── softmatch
│   └── brother
└── src
    ├── hard_match
    ├── raw_data_process
    ├── rule_mining
    └── softmatch
```