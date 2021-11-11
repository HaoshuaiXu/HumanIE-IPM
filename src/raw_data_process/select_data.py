import pandas as pd


def select_by_relationid_from_opendata(datafilepath, to_select_relation_id:str, savedfilepath):
    dataset = pd.read_csv(
        filepath_or_buffer=datafilepath, 
        sep='\t',
        names=['sent_id', 'relation_id']
        )
    sent_id = dataset[dataset['relation_id'] == str(to_select_relation_id)]['sent_id'] # to_select_relation_id 在数据集中被识别为了字符串类型
    sent_id.to_csv(savedfilepath, index=False)
    
    

if __name__ == '__main__':
    open_data_filepath = "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/raw_data/open_data(all)/sent_relation_train.txt"
    select_by_relationid_from_opendata(
        datafilepath=open_data_filepath,
        to_select_relation_id='1',
        savedfilepath="/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/select_data/open_data_friend_sent_id.csv"
    )