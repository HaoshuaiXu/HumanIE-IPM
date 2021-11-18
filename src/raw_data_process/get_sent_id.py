import pandas as pd


def select_by_relationid_from_opendata(datafilepath, to_select_relation_id:str, savedfilepath):
    """
    datafilepath: open data 文件地址
    to_select_relation_id: 需要的关系序号
    savedfilepath: 筛选出的句子序号所保存的文件地址
    """
    
    dataset = pd.read_csv(
        filepath_or_buffer=datafilepath, 
        sep='\t', # open data 所用的分隔符是制表符
        names=['sent_id', 'relation_id'] # 原来的文件中没有字段名，因此将字段命名为 sent_id 和 relation_id
        )
    sent_id = dataset[dataset['relation_id'] == str(to_select_relation_id)]['sent_id'] # to_select_relation_id 在数据集中被识别为了字符串类型
    # 上一个语句是来进行筛选的语句，下一个语句是将数据写入硬盘的语句
    sent_id.to_csv(savedfilepath, index=False)
    
    

if __name__ == '__main__':
    open_data_filepath = "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/raw_data/open_data(all)/sent_relation_train.txt"
    saved_filepath = "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/select_data_sent_id/open_data_parentschild_13.csv"
    select_by_relationid_from_opendata(
        datafilepath=open_data_filepath,
        to_select_relation_id="13",
        savedfilepath=saved_filepath,
        )