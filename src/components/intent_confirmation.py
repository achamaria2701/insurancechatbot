from src.utils import get_chat_completions

class IntentConfirmation:

    def __init__(self):
        pass

    def get_intent_confirmation(self, response_assistant):

        delimiter = "####"

        allowed_values = {'Yes','No'}

        prompt = f"""
        You are a senior evaluator who has an eye for detail.The input text will contain a user requirement captured through 7 keys.
        You are provided an input. You need to evaluate if the input text has the following keys:
        {{
        'Coverage Amount': "values",
        'Daycare Procedures Covered':"values",
        'Critical Illness Cover': "values",
        'Co-payment' : "values",
        'Family Floater': "values",
        'Pre/Post Hospitalization Cover': "values",
        'Maternity Cover': "values"
        }}
        The values for the keys except 'Coverage Amount' should only be from the allowed values: {allowed_values}.
        The 'Coverage Amount' key can take only a numerical value.
        Next you need to evaluate if the keys have the the values filled correctly.
        Only output a one-word string in JSON format at the key 'result' - Yes/No.
        Thought 1 - Output a string 'Yes' if the values are correctly filled for all keys, otherwise output 'No'.
        Thought 2 - If the answer is No, mention the reason in the key 'reason'.
        Thought 3 - Think carefully before the answering.
        
        Here is the input: {response_assistant}
        Only output a one-word string - Yes/No.
        """
        
        messages = [{"role": "system", "content": prompt}]
        confirmation = get_chat_completions(messages)

        return confirmation