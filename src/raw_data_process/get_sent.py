import pandas as pd


if __name__ == '__main__':
    sent_train = pd.read_csv(
        filepath_or_buffer="/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/raw_data/open_data(all)/sent_train.txt", 
        sep='\t',
        names=['sent_id', 'entity1', 'entity2', 'sent']
        )
    
    sent_id_set = pd.read_csv(
        filepath_or_buffer="/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_id/opendata_couple_all.csv",
        sep='\t',
        names=['sent_id']
    )
    
    pd.merge(
        left=sent_id_set,
        right=sent_train,
        on='sent_id'
        ).to_csv(
            "/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set/couple_test.csv",
            index=False
        )