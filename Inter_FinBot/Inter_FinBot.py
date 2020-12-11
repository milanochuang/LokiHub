#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

import requests
try:
    from intent import Loki_Exchange
except:
    from .intent import Loki_Exchange

from ArticutAPI import ArticutAPI

articut = ArticutAPI.Articut()


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "peter.w@droidtown.co"
LOKI_KEY = "zhQi3kkkS$z^Ssv&$YsK4oYrXz6F@ab"
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []
    

    def __init__(self, inputLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []

        try:
            result = requests.post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": INTENT_FILTER
            })

            if result.status_code == requests.codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst
    def amountSTRConvert(self, inputSTR):
        resultDICT = articut.parse(inputSTR, level="lv3")
        return resultDICT["number"]
    
def runLoki(inputLIST):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Exchange
                if lokiRst.getIntent(index, resultIndex) == "Exchange":
                    resultDICT = Loki_Exchange.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def getTodayExchangeRage():
    response = requests.get("https://tw.rter.info/capi.php")
    rateDICT = response.json()
    return rateDICT

def moneyName(inputSTR):
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
        return moneyDICT[inputSTR]
def amountSTRConvert(inputSTR):
    resultDICT={}
    if(inputSTR == None):
        resultDICT["number"] = 1
    else:
        resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT["number"]

if __name__ == "__main__":
    inputLIST = ["100台幣換美金"]
    resultDICT = runLoki(inputLIST)
    print("Result => {}".format(resultDICT))
    print(resultDICT['src'])
    src = moneyName(resultDICT["src"])
    tgt = moneyName(resultDICT["tgt"])
    amt = amountSTRConvert(resultDICT['amt'])[resultDICT['amt']]
    
    