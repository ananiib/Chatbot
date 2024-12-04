# Chatbot using DialoGPT💻💬✨

This is a Python-based chatbot application using  **DialoGPT** (a variant of GPT-2 by Microsoft), a conversational model fine-tuned from GPT-2 for generating human-like dialogues. 
The chatbot is designed to engage users in a casual conversation, providing responses to various inputs.
The chatbot is trained on the **Daily Dialog** dataset and includes preprocessing techniques like text cleaning to handle special characters and make the dialogues consistent for training.

## Features🫧
- **Text Cleaning**: The chatbot preprocesses input text by converting it to lowercase and removing special characters.This ensures more consistent and cleaner inputs for the model.
- **Chatbot Interactive Chat**: Users can interact with the chatbot by typing a message and receiving a generated response.
- **Conversational Model**: Uses DialoGPT-medium for generating human-like dialogues based on user input.
- **Demonstration of Text Cleaning**: Users can type any sentence to see how the text cleaning function works before being processed by the chatbot.
- **MIT License**: The project is open-source and licensed under the MIT License.

  ## How It Works:
1. ### Text Cleaning:
   - Each input is passed through a function that removes any non-alphanumeric characters and trims unnecessary spaces.
3. ### Chatbot Interaction:
   - After cleaning the input, the processed text is passed to the DialoGPT model, which generates an appropriate response.
5. ### Interactive Mode:
   - The chatbot keeps interacting with the user until the user types "exit."

## Libraries Used:
- torch
- transformers
- datasets
- re (*regular expressions* for text cleaning)

## Getting Started📝

### Prerequisites
Ensure that you have **Python 3.11** installed. You will also need to install the required dependencies.

### Installing Dependencies

1. Clone the repository:
    ```bash
    git clone https://github.com/ananiib/Chatbot_Project.git
    cd Chatbot_Project
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Chatbot🤖

To run the chatbot:

1. Ensure that the virtual environment is activated.
2. Run the `chatbot.py` script:
    ```bash
    python chatbot.py
    ```

### Text Cleaning Demonstration

Before the chatbot starts, you can test the text cleaning functionality. Type sample text, and the program will show how it cleans the text by removing special characters and normalizing the input.

### Example Interaction

```txt
Enter a sample text: HELLO WORLD! How's it going?
Original: HELLO WORLD! How's it going?
Cleaned: hello world hows it going
```
```txt
Enter a sample text: HEYY xd i love shopping 🛍️💸$$!! <3.
Original: HEYY xd    i love $shopping 🛍️💸$$!! <3.
Cleaned: heyy xd i love shopping
Enter a sample text: exit
```
```
Exiting text cleaning demo.
```

### Chatbot Interaction

```
Chatbot is ready! Type 'exit' to quit.
```
```txt
You: Heyy chatbot!
Chatbot: Hi! How can I assist you today?

You: What is your name?
Chatbot: I am DialoGPT, your friendly chatbot. How can I help you?

You: What is the weather like today?
Chatbot: I'm sorry, I can't provide real-time weather information, but I'm happy to chat about other topics!

You: exit
Goodbye!
```

