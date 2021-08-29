import json
import jieba
import pandas as pd
#

types = ['套餐', '网速', '信号', '流量', '客服', '投诉', '@', '宽带', '套路', '网不好'
                                                              '短线', '诈骗', '垃圾', '扣费', '服务态度']

# ignore user list
ignr_usrlist = []

# ignore keyword list
ignr_kwlist = ['链接', '点击', 'IOS应用', '合作', '招标公告', '助力', '印度', '携手', ]


def test_msg_ana(_file_name: str):
    data_file = open(_file_name, 'r', encoding='UTF-8')
    data_collect = json.load(data_file, encoding='UTF-8')
    data_file.close()
    cnt1 = 0
    cnt2 = 0
    sample_num = len(data_collect)
    for data in data_collect[:sample_num]:
        if str(data['userId']) in ignr_usrlist:
            # data['ignore'] = 1
            data_collect.remove(data)
            continue
        msg = data['msg']
        # print(jieba.lcut(msg))
        # lcut = jieba.lcut(msg)

        for word in ignr_kwlist:
            if word in msg:
                # data['ignore'] = 1
                data_collect.remove(data)
                break
        else:
            # data['ignore'] = 0
            cnt1 += 1
            # for word in types:
            #     if word in msg:
            #         # data['ignore'] = 1
            #         data_collect.remove(data)
            #         break
            # else:
            #     cnt2 += 1
    print(cnt1)
    print(round(cnt1 / sample_num, 2))
    print(cnt2)
    print(round(cnt2 / cnt1, 2))

    df = pd.DataFrame(data_collect)
    df.to_excel('test_msg.xlsx', index=False)


if __name__ == '__main__':
    js_file_name = 'test_data.json'
    test_msg_ana(js_file_name)
