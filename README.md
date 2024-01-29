# Quiz Generator Script

## Overview

This script is designed to generate quiz-like questions on a variety of subjects. It uses the Hugging Face Inference API to create questions in a multiple-choice format. The user can input a subject, and the script will output a question with four options and the correct answer.

## Requirements

- Python 3.x
- Hugging Face account and API token

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/ClementFrvl/quiz-game-decentralization
   ```

2. **Install Dependencies**: Install the necessary Python packages.

   ```bash
   pip install huggingface_hub
   ```

3. **Environment Variables**: Set up an environment variable for the Hugging Face API token. You can get this token from your Hugging Face account.

   ```bash
   export INFERENCE_TOKEN='your_huggingface_api_token'
   ```

## Usage

1. **Run the Script**: Execute the script in your Python environment.

   ```bash
   python quiz_generator.py
   ```

2. **Enter a Subject**: When prompted, input the subject you want to generate a quiz question for.

3. **Get the Quiz Question**: The script will output a multiple-choice question related to the subject you entered.

## Example

Input:
```
What subject do you want to learn about? history
```

Output:
```
Here is a short quiz-like question on history: [Question and options will be displayed here]
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.
