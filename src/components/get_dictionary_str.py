import openai
import apikey

openai.api_key = apikey.OPENAI_API_KEY

class GetDictionaryString():

    def __init__(self):
        pass

    def getDictionary(self, response):
        delimiter = "####"

        user_req = {'Coverage Amount': "500000",
                    'Daycare Procedures Covered':"Yes",
                    'Critical Illness Cover': "No",
                    'Co-payment' : "Yes",
                    'Family Floater': "No",
                    'Pre/Post Hospitalization Cover': "No",
                    'Maternity Cover': "Yes"}

        prompt = f"""You are a python expert. You are provided an input.
                You have to check if there is a python dictionary present in the string.
                It will have the following format {user_req}.
                Your task is to just extract the relevant values from the input and return only the python dictionary in JSON format.
                The output should match the format as {user_req}.
        
                {delimiter}
                The output should contain the exact keys and values as present in the input.
                Ensure the keys and values are in the given format:
                {{'Coverage Amount': "500000",
                'Daycare Procedures Covered':"Yes/No",
                'Critical Illness Cover': "Yes/No",
                'Co-payment' : "Yes/No",
                'Family Floater': "Yes/No",
                'Pre/Post Hospitalization Cover': "Yes/No",
                'Maternity Cover': "Yes/No"}}
            
                Here are some sample input output pairs for better understanding:
                {delimiter}
                input 1: -Coverage Amount: "500000" -Daycare Procedures Covered:"Yes" -Critical Illness Cover: "No" -Co-payment : "Yes" -Family Floater: "No" -Pre/Post Hospitalization Cover: "No" -Maternity Cover: "Yes"
                output 1: {{'Coverage Amount': "500000", 'Daycare Procedures Covered':"Yes", 'Critical Illness Cover': "No", 'Co-payment' : "Yes", 'Family Floater': "No", 'Pre/Post Hospitalization Cover': "No", 'Maternity Cover': "Yes"}}

                input 2: {{'Coverage Amount':    "600000", 'Daycare Procedures Covered':   "No", 'Critical Illness Cover':    "Yes", 'Co-payment' :  "Yes", 'Family Floater': "Yes", 'Pre/Post Hospitalization Cover':     "No", 'Maternity Cover':"No"}}
                output 2: {{'Coverage Amount': "600000", 'Daycare Procedures Covered':"No", 'Critical Illness Cover': "Yes", 'Co-payment' : "Yes", 'Family Floater': "Yes", 'Pre/Post Hospitalization Cover': "No", 'Maternity Cover': "No"}}
                
                input 3: Great! Based on your responses, here is the updated insurance profile: {{'Coverage Amount': '700000', 'Daycare Procedures Covered': 'No', 'Critical Illness Cover': 'Yes', 'Co-payment': 'Yes', 'Family Floater': 'No', 'Pre/Post Hospitalization Cover': 'Yes', 'Maternity Cover': 'Yes'}}
                output 3: {{'Coverage Amount': "700000", 'Daycare Procedures Covered':"No", 'Critical Illness Cover': "Yes", 'Co-payment' : "Yes", 'Family Floater': "No", 'Pre/Post Hospitalization Cover': "Yes", 'Maternity Cover': "Yes"}}
                {delimiter}
                """
        messages = [{"role": "system", "content":prompt },
                    {"role": "user", "content":f"""Here is the user input: {response}""" }]

        confirmation = openai.chat.completions.create(
                                        model="gpt-3.5-turbo",
                                        messages = messages,
                                        response_format={ "type": "json_object" },
                                        seed = 1234)

        output = confirmation.choices[0].message.content
        return output