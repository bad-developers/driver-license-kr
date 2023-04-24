import json
import pymongo
import re

if __name__ == "__main__":
    # my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    my_db = my_client["driver"]
    my_col = my_db["question"]
    question_head = "QQQ"
    answer_head = "QAA"
    correct_answer = "AAA"
    end_line_head = "%%%"
    my_dict = {}
    count = 1
    with open("../question_short.txt", "r", encoding="utf8") as file:
        for cur_line in file:
            if "\n" in cur_line:
                cur_line = cur_line.replace('\n', '')

            if question_head in cur_line:
                my_dict["question_id"] = count
                my_dict["question"] = {
                    "id": count,
                    "text": cur_line.replace(question_head, ''),
                    "type": "Sentence type 1 answer",
                    "media": ""
                }
            elif answer_head in cur_line:
                if "answerList" not in my_dict:
                    my_dict["answerList"] = []

                my_dict["answerList"].append({
                    "id": len(my_dict["answerList"]) + 1,
                    "text": cur_line.replace(answer_head, '')
                })
            elif correct_answer in cur_line:
                my_dict["correctAnswer"] = cur_line.replace(correct_answer, '')
            elif end_line_head in cur_line:
                x = my_col.insert_one(my_dict.copy())
                print(count)
                count = count + 1
                my_dict = {}
