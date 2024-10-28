import openai
import ast
import regex as re
import apikey

openai.api_key = apikey.OPENAI_API_KEY


def get_chat_completions(input):
    MODEL = 'gpt-3.5-turbo'
    chat_completion = openai.chat.completions.create(
        model= MODEL,
        messages= input,
        seed = 1234)
    output = chat_completion.choices[0].message.content
    return output

def moderation_check(user_input):
    response = openai.moderations.create(
        model="omni-moderation-latest",
        input= user_input)
    
    moderation_output = response.results[0]
    
    for key, value in moderation_output:
        if value == True:
            return "Flagged"
    return "Not Flagged"

def extract_dictionary_from_string(string):
    regex_pattern = r"\{[^{}]+\}"

    dictionary_matches = re.findall(regex_pattern, string)

    # Extract the first dictionary match and convert it to lowercase
    if dictionary_matches:
        dictionary_string = dictionary_matches[0]
        #dictionary_string = dictionary_string.lower()

        # Convert the dictionary string to a dictionary object using ast.literal_eval()
        dictionary = ast.literal_eval(dictionary_string)
    return dictionary