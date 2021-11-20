# 数据文件夹说明

- raw_data: 用于存放 open data 数据集的所有源文件；未经任何处理
- opendata_sent_id: 用于存放根据"raw_data/open_data(all)/relation2id.txt"从筛选出来的需要关系的句子序号
- opendata_sent_set: 用于存放根据 sent id 从“raw_data/open_data(all)/sent_train.txt”筛选出来的对应关系的句子
- opendata_sent_set_replace-entity: 替换实体后的句子
- opendata_sent_set_remove-stopwords: 去除中英文标点、阿拉伯数字、英文字符、中文停用词后的句子
- sent_train: 训练集，句子有人工标注的标签，用于挖掘种子规则、训练验证模型
- sent_test: 测试集，句子没有人工标注的标签，用于规则挖掘迭代
- sent_veri: 验证集，句子有人工标注的标签，用于验证规则

## 数据分配

| 数据集名称 | 训练集 | 测试集 | 验证集 | 总数 |
| --- | --- | --- | --- | --- |
| brother & teacher | 1000 | 3800 | 1999 | 6799 |
| couple & parentschild | 1000 | 16065 | 7312 | 24377 |
| friend & parentschild | 1000 | 1324 | 696 | 3020 |