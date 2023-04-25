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
    description_head = "DDD"
    correct_answer = "AAA"
    end_line_head = "%%%"
    my_dict = {}
    count = 1
    with open("../question_short.txt", "r", encoding="utf8") as file:
        for cur_line in file:
            if "\n" in cur_line:
                cur_line = cur_line.replace('\n', '')

            if question_head in cur_line:

                cur_line = cur_line.replace(question_head, '')
                question_id = re.search(r'^\d+', cur_line).group()
                my_dict["question_id"] = question_id
                my_dict["question_type"] = {
                    "type": "Text Only",
                    "detail": "Question type 1 answer",
                    "url": ""
                }
                my_dict["question"] = {
                    "text": cur_line,
                }

            elif answer_head in cur_line:
                cur_line = cur_line.replace(answer_head, '')
                if "answer_list" not in my_dict:
                    my_dict["answer_list"] = []

                my_dict["answer_list"].append({
                    "id": len(my_dict["answer_list"]) + 1,
                    "text": cur_line
                })

            elif description_head in cur_line:
                cur_line = cur_line.replace(description_head, '')
                if "description_list" not in my_dict:
                    my_dict["description_list"] = []
                my_dict["description_list"].append({
                    "id": len(my_dict["description_list"]) + 1,
                    "text": cur_line
                })
                my_dict["question_type"] = {
                    "type": "With Media",
                    "detail": "",
                    "url": ""
                }

            elif correct_answer in cur_line:
                cur_line = cur_line.replace(correct_answer, '')
                my_dict["correct_answer"] = cur_line

            elif end_line_head in cur_line:
                x = my_col.insert_one(my_dict.copy())
                print(count)
                count = count + 1
                my_dict = {}
