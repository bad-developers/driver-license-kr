import json
import pymongo
import re

if __name__ == "__main__":
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["driver"]
    my_col = my_db["test"]
    question_head = "QQQ"
    answer_head = "QAA"
    correct_answer = "AAA"
    end_line_head = "%%%"
    my_dict = {}

    with open("../question_short.txt", "r", encoding="utf8") as file:
        for line in file:
            if "\n" in line:
                line = line.replace('\n', '')

            if question_head in line:
                my_dict["question"] = {
                    "id": 1,
                    "text": line.replace(question_head, ''),
                    "type": "Sentence type 1 answer",
                    "media": ""
                }
            elif answer_head in line:
                if "answerList" not in my_dict:
                    my_dict["answerList"] = []

                my_dict["answerList"].append({
                    "id": len(my_dict["answerList"]),
                    "text": line.replace(answer_head, '')
                })
            elif 'AAA' in line:
                # x = mycol.insert_one(mydict)
                my_dict["correctAnswer"] = line.replace(correct_answer, '')
            elif "%%%" in line:
                # x = mycol.insert_one(mydict)
                # mydict = {}

                print("aaaa")
