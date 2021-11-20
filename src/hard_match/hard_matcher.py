import pandas as pd
import re


def ruleset2wordlist(rule_set):
    """
    将规则集中的每个规则从字符串变成列表，以规则的词作为每个列表中的单个元素。
    """
    rule_word_list_set = []
    for rule in rule_set:
        rule_word_list_set.append(rule.split())
    return rule_word_list_set

def construct_pattern(rule):
    pattern = ''
    for w in rule:
        pattern = pattern + '.*' + w
    result = pattern + '.*'
    return result


if __name__ == '__main__':

    iterative_num = '1'
    relation_name = 'teacher'

    # 数据准备。读取规则集和句子集.
    rule_set = pd.read_csv(
        '/Users/xuhaoshuai/GitHub/HumanIE_IPM/labeled_rule/' + relation_name +'/' + iterative_num + '.csv'
        )
    sent_set = pd.read_csv(
        '/Users/xuhaoshuai/GitHub/HumanIE_IPM/data/sent_test/' + relation_name + '.csv',
        names=['sent']
        )
    
    # 新增列，标注列
    sent_set['hard_match'] = 'NaN'

    # 先筛选正、负规则
    negative_rules = rule_set[rule_set['label'] == 0]['rule'].to_list()
    positive_rules = rule_set[rule_set['label'] == 1]['rule'].to_list()

    # 先用负例做硬匹配
    for index, row in sent_set.iterrows():
        for rule in ruleset2wordlist(negative_rules):
            pattern = construct_pattern(rule)
            hard_match = re.search(pattern=pattern, string=row['sent'])
            if hard_match:
                row['hard_match'] = 0
                break
    sent_set[sent_set['hard_match'] == 0].to_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/hard_match/neg/" + relation_name + "/" + iterative_num + ".csv",
        index=None
    )
    # 再用正例做硬匹配
    remaining_sent_set = sent_set[sent_set['hard_match'] != 0]
    for index, row in remaining_sent_set.iterrows():
        for rule in ruleset2wordlist(positive_rules):
            pattern = construct_pattern(rule)
            hard_match = re.search(pattern=pattern, string=row['sent'])
            if hard_match:
                row['hard_match'] = 1
                break
    remaining_sent_set[remaining_sent_set['hard_match'] == 1].to_csv(
        "/Users/xuhaoshuai/GitHub/HumanIE_IPM/hard_match/pos/" + relation_name + "/" + iterative_num + ".csv",
        index=None
    )
    # 最后剩余的输出
    remaining_sent_set[
        remaining_sent_set['hard_match'] != 1
        ].to_csv(
            "/Users/xuhaoshuai/GitHub/HumanIE_IPM/hard_match/none/" + relation_name + "/" + iterative_num + ".csv",
            index=None
        )

    # for sent in sent_set['sent'].to_list():
    #     for rule in ruleset2wordlist(negative_rules):
    #         pattern = ''
    #         for w in rule:
    #             pattern = pattern + '.*' + w
    #         pattern = pattern + '.*'
    #         hard_match = re.search(pattern=pattern, string=sent)
    #         if hard_match:
    #             print(sent + ': 1')
    #             pass
    #         else:
    #             # print('0')
    #             pass
    
    # rule_set = []
    # for rule in rules.to_list():
    #     rule_set.append(rule.split())


    # for sent in sent_set:
    #     for rule in rule_set:
    #         pattern = ''
    #         for w in rule:
    #             pattern = pattern + '.*' + w
    #         pattern = pattern + '.*'
    #         hard_match = re.search(pattern=pattern, string=sent)



    # sentence = "人物二 带领 弟子 周游列国 经历 新郑 之病 不得不 住 几月 弟子 人物一 问 人物二 干 农活"
    # rule_word = ["人物二", "经历", "弟子"]
    # pattern = ''
    # for w in rule_word:
    #     pattern = pattern + '.*' + w
    # pattern = pattern + '.*'

    # end = re.search(pattern=pattern, string=sentence)
    # if end.span():
    #     print(end)
    # else:
    #     pass
