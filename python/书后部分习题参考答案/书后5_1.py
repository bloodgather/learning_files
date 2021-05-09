# -*- coding: utf-8 -*-
"""

课后习题 第五章 （1）

"""

# create with roommates information
dicTXL = {
            "小新": {
                        "手机": 13913000001,
                        "QQ": 18191220001,
                    },
            "小亮": {
                        "手机": 13913000002,
                        "QQ": 18191220002,
                    },
            "小刚": {
                        "手机": 13913000003,
                        "QQ": 18191220003,
                    }
         }

# create neighbour information  
dicOther = {
            "大刘": {
                        "手机": 13914000001,
                        "QQ": 18191230001,
                    },
            "大王": {
                        "手机": 13914000002,
                        "QQ": 18191230002,
                    },
            "大张": {
                        "手机": 13914000003,
                        "QQ": 18191230003,
                    }
           }

# merge two dictionaries together
dicTXL.update(dicOther)

# create existing WeChat information dictionary
dicWX = {
            "小新": "xx9907",
            "小刚": "gang1004",
            "大王": "jack_w",
            "大刘": "liu666",
        }

# merge WeChat information into dicTXL
for key, value in dicTXL.items():
    if key in dicWX.keys():
        WX_value = dicWX[key]
    else:
        WX_value = str(value["手机"])
    value.update({"微信号": WX_value})

print(dicTXL)

# TEST 1: change
dicTXL["大王"]["手机"] = 13914000004

print(dicTXL)

# TEST 2: search
name = input("请输入姓名：")
if name in dicTXL.keys():
    communication = input("请输入联系方式（手机，QQ，微信号）")
    if communication in dicTXL[name].keys():
        print(dicTXL[name][communication])
else:
    print("没有该同学的联系方式")