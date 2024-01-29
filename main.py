#!/usr/bin/env python
from huggingface_hub import InferenceClient, login
import os
import json

def parse_quiz(quiz_string):
    parts = quiz_string.split('\n')
    json_strings = ["{"]
    for line in parts:
        if line == "}":
            json_strings[-1] += line
            json_strings.append("")
        elif line == "{":
            json_strings[-1] += line
        elif json_strings[-1] != "":
            json_strings[-1] += line

    parsed_quiz = [json.loads(json_string) for json_string in json_strings if json_string != "" and json_string[-1] == "}"]

    return parsed_quiz

a = input("What subject do you want to learn about? ").strip().lower()

client = InferenceClient(token=os.environ["INFERENCE_TOKEN"])
question_number = 1

output = client.text_generation("""Here is the first question of a short quiz about '""" + a + """', in the json format: {'question': '...', "options": [{'id': 'A', 'question': 'Question A'}, {'id': 'B', 'question': 'Question B'} ...] , 'answer': A }.\n\nQuestion #""" + str(question_number) + """:\n{""", max_new_tokens=500)

quiz = parse_quiz(output)

for quiz_question in quiz:
    print(f"\nQuestion #{question_number}:")
    print(quiz_question["question"] + "\n")

    for option in quiz_question["options"]:
        print(option["id"] + ") " + option["question"])

    answer = input("What is your answer? ").strip().lower()

    if answer == quiz_question["answer"].strip().lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is " + [a["question"] for a in quiz_question["options"] if a["id"] == quiz_question["answer"]][0] )

    question_number += 1