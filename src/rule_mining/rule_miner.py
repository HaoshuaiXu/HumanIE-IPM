from prefixspan import PrefixSpan

with open("/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/opendata_sent_set_remove-stopwords/brother.csv", "r") as f:
    db = [i.strip('\n') for i in f.readlines()]

ps = PrefixSpan(db)
