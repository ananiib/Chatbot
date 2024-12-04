import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
import re

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


tokenizer.pad_token = tokenizer.eos_token

input_text = "User: hey\nBot:"


dataset = load_dataset("daily_dialog", trust_remote_code=True)
train_data = dataset["train"]


def preprocess_text(dialog):
    """
    Preprocesses a single dialog by converting it to lowercase and cleaning up special characters.
    Each dialog is a list of sentences, so we process each sentence individually.
    """
    dialog = [sentence.lower() for sentence in dialog]
    dialog = [remove_special_characters(sentence) for sentence in dialog]
    return dialog

def remove_special_characters(text):
    """
    Removes special characters and extra spaces from the text.
    """
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

train_data = train_data.map(lambda x: {"dialog": preprocess_text(x["dialog"])})

print("Example of a preprocessed dialog:", train_data["dialog"][0])

def demonstrate_text_cleaning():
    """
    Show examples of how the text cleaning works.
    Takes user input, applies cleaning, and displays the result.
    """
    print("\nText Cleaning Demonstration! Type 'exit' to stop.")
    while True:
        user_input = input("Enter a sample text: ")
        if user_input.lower() == "exit":
            print("Exiting text cleaning demo.")
            break

        cleaned_text = remove_special_characters(user_input.lower())
        print(f"Original: {user_input}")
        print(f"Cleaned: {cleaned_text}")
        print("-" * 40)

def generate_response(input_text):
    inputs = tokenizer(
        input_text + tokenizer.eos_token,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    # Generate a response
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        pad_token_id=tokenizer.pad_token_id,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )

    # Decode and clean the response
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = generated_text[len(input_text):].strip()
    return response

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    # First demonstrate text cleaning
    demonstrate_text_cleaning()
    # Then proceed to run the chatbot
    chatbot()
