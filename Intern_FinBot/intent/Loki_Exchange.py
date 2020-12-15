#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Exchange = True
userDefinedDICT = {}
moneyDICT = {
                    "台幣": "TWD",
                    "歐元": "EUR",
                    "美金": "USD",
                    "日幣": "JPY",
                    "人民幣": "CNH",
                    "基普": "LAK", #寮國
                    "墨西哥披索": "MXN",
                    "里亞爾": "IRR", #伊朗
                    "冰島克朗": "ISK", #冰島
                    "拉特": "LVL", #拉脫維亞
                    "愛爾蘭鎊": "IEP",
                    "開曼元": "KYD",
                    "烏拉圭披索": "UYU",
                    "斐濟幣": "FJD",
                    "加幣": "CAD",
                    "令吉": "MYR", #馬拉西亞
                    "倫皮拉": "HNL", #宏都拉斯
                    "瑞典克朗": "SEK",
                    "埃及鎊": "EGP",
                    "古巴披索": "CUP",
                    "英鎊": "GBP",
                    "捷克克朗": "CZK",
                    "里拉": "TRY", #土耳其
                    "列弗": "BGN", #保加利亞
                    "瑞士法郎": "CHF",
                    "汶萊元": "BND",
                    "茲羅提": "PLN", #波蘭
                    "黎巴嫩鎊": "LBP",
                    "迪拉姆": "AED", #阿聯
                    "塔卡": "BDT", #孟加拉
                    "庫納": "HRK", #克羅埃西亞
                    "澳門幣": "MOP",
                    "丹麥克朗": "DKP",
                    "挪威克朗": "NOK",
                    "列伊": "RON", #羅馬尼亞
                    "澳元": "AUD", 
                    "新加坡幣": "SGD", 
                    "韓元": "KRW",
                    "韓圜": "KRW",
                    "斯里蘭卡盧比": "LKR" ,
                    "以色列幣": "ILS",
                    "巴基斯坦盧比": "PKR",
                    "阿根廷披索": "ARS",
                    "瑞爾": "KHR", #柬埔寨
                    "索爾": "PEN", #秘魯
                    "紐西蘭元": "NZD",
                    "越南盾": "VND",
                    "南非鍰": "ZAR",
                    "西非法郎": "XOF",
                    "中非法郎": "XAF",
                    "印尼盧比": "IDR",
                    "智利披索": "CLP",
                    "福林": "HUF", #匈牙利
                    "泰銖": "THB",
                    "盧布": "BYR", #白俄羅斯
                    "港幣": "HKD",
                    "印度盧比": "INR",
                    "黑奧": "BRL", #巴西
                }

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[100元][美金]可以兌換[台幣]多少":
        # write your code here
        resultDICT["src"] = args[1]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[0]
        pass

    if utterance == "[100元][美金]可以兌換多少[台幣]":
        # write your code here
        resultDICT["src"] = args[1]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[0]
        pass

    if utterance == "[100元][美金]要[台幣]多少":
        # write your code here
        resultDICT["src"] = args[1]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[0]
        pass

    if utterance == "[100元][美金]要多少[台幣]":
        # write your code here
        resultDICT["src"] = args[1]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[0]
        pass

    if utterance == "[100台幣]換[美金]":
        # write your code here
        resultDICT["src"] = [x for x in moneyDICT if x in args[0]][0] #把值從DICT裡拿出來，確認值跟目標值是否一致
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[0]        
        pass

    if utterance == "[100美金]能換多少[台幣]":
        # write your code here
        resultDICT["src"] = [x for x in moneyDICT if x in args[0]][0] #把值從DICT裡拿出來，確認值跟目標值是否一致
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[0]    
        pass

    if utterance == "[100美金]要[台幣]多少":
        # write your code here
        resultDICT["src"] = [x for x in moneyDICT if x in args[0]][0] #把值從DICT裡拿出來，確認值跟目標值是否一致
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[0]    
        pass

    if utterance == "[100美金]要多少[台幣]":
        # write your code here
        resultDICT["src"] = [x for x in moneyDICT if x in args[0]][0] #把值從DICT裡拿出來，確認值跟目標值是否一致
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[0]    
        pass

    if utterance == "[今天][美金]兌換[台幣]是多少":
        # write your code here
        pass

    if utterance == "[我]想要[100元][美金]":
        # write your code here
        resultDICT["src"] = "台幣"
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[我]想要[美金][100元]":
        # write your code here
        resultDICT["src"] = "台幣"
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[2]
        pass

    if utterance == "[我]想買[100元][美金]":
        # write your code here
        resultDICT["src"] = "台幣"
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[我]想買[美金][100元]":
        # write your code here
        resultDICT["src"] = "台幣"
        resultDICT["tgt"] = args[1]
        resultDICT["amt"] = args[2]

    if utterance == "[美金][100]要[台幣]多少":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[美金][100]要多少[台幣]":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[美金][100元]可以兌換[台幣]多少":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[美金][100元]可以兌換多少[台幣]":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[美金][100元]要[台幣]多少":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]
        pass

    if utterance == "[美金][100元]要多少[台幣]":
        # write your code here
        resultDICT["src"] = args[0]
        resultDICT["tgt"] = args[2]
        resultDICT["amt"] = args[1]

    return resultDICT