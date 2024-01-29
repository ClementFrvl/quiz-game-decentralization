#!/usr/bin/env python
from huggingface_hub import InferenceClient, login
import os

a = input("What subject do you want to learn about? ").strip().lower()

client = InferenceClient(token=os.environ["INFERENCE_TOKEN"])
output = client.text_generation(f"Here is a 100-token quiz like question on {a}, in the format: Question - Option A - Option B - Option C - Option D - Correct option (A/B/C/D):", max_new_tokens=150)

def parse_quiz(quiz_string):
    parts = quiz_string.split('\n')

    # Find the index of the question
    question_index = next(i for i, line in enumerate(parts) if line.startswith('Question'))

    # Find the indices of the options
    options_indices = [i for i, line in enumerate(parts[question_index+1:], start=question_index+1) if line.strip()]

    print(options_indices)

    quiz = {
        'question': parts[question_index],
        'options': {
            'A': parts[options_indices[0]],
            'B': parts[options_indices[1]],
            'C': parts[options_indices[2]],
            'D': parts[options_indices[3]],
        },
        'correct_option': parts[options_indices[4]].split()[-1]
    }

    return quiz

# Test the function
print(parse_quiz(output))

