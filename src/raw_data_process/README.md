# 项目结构

- get_sent_id.py: 由于 Open data 数据集句子及其人物关系不在一个文件中，而是用另一个“sentid-relationid”文件单独标明了句子序号及其对应的关系类型序号，所以需要从“sentid-relationid”中挑出我们需要的关系的句子序号。这个文件就是来进行这一步处理的。
- get_sent.py: 从 sent_train.txt 中根据 sent id 抽取句子。
- replace_entity.py: 替换实体

# 已知问题

1. 使用`get_sent.py`获取句子的时候，couple 关系的句子会出现问题。表现在`/data/opendata_sent_set/couple.csv`下大部分句子以逗号作为分隔符，而 323-1060 条句子还是以制表符作为分隔符。