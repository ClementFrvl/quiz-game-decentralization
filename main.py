from huggingface_hub import InferenceClient, login
import os

a = input("What subject do you want to learn about? ").strip().lower()

client = InferenceClient(token=os.environ["INFERENCE_TOKEN"])
output = client.text_generation(f"Here is a short quiz like question on {a}, in the format: Question - Option A - Option B - Option C - Option D - Correct option (A/B/C/D):", max_new_tokens=100)

print(output)