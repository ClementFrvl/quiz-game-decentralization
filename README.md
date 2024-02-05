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
   pip install -r requirements.txt
   ```

3. **Environment Variables**: Set up an environment variable for the Hugging Face API token. You can get this token from your Hugging Face account.

   ```bash
   export INFERENCE_TOKEN='your_huggingface_api_token'
   ```

## Usage

1. **Run the Script**: Execute the script in your Python environment.

   ```bash
   python3 main.py
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

Contributions are welcome! If you have a bug to report, a feature to suggest, or a patch to contribute, please feel free to do so.

To contribute, you can fork the repository, make your changes, and then submit a pull request. Please make sure to include a detailed description of your changes.

If you're reporting a bug, please include as much information as possible about the issue, including the steps to reproduce it, the expected behavior, and the actual behavior.

If you're suggesting a feature, please provide a detailed description of the feature and why you think it would be useful.
