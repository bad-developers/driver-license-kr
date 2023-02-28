import json
import pymongo
import re

if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    mydb = myclient["driver"]
    mycol = mydb["test"]

    #       {
    #         "question": {
    #           "id": 1,
    #           "text": "asdf",
    #           "type": "questionType",
    #           "media": ""
    #         },
    #         "answerList": [
    #           {
    #             "id": 1,
    #             "text": "D"
    #           },

    mydict = {
    }

    with open("../question_short.txt", "r") as file:
        for line in file:
            if 'QQQ' in line:
                mydict["question"] = {
                    "id": 1,
                    "text": line,
                    "type": "Sentence type 1 answer",
                    "media": ""
                }
            elif 'AAA' in line:
                if not isinstance(mydict["answerList"], list):
                    mydict["answerList"] = []

                mydict["answerList"].append({
                    "id": len(mydict["answerList"]),
                    "text": line
                })
            elif 'DDD' in line:
                # x = mycol.insert_one(mydict)
                # mydict = {}
            elif '%%%' in line:
                # x = mycol.insert_one(mydict)
                # mydict = {}

                print("aaaa")

