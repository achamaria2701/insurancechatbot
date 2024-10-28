class ConvRecommendation():

    def __init__(self):
        pass

    def initialize_conv_reco(self, products):
        system_message = f"""
        You are an intelligent insurance expert and you are tasked with the objective to \
        solve the user queries about any product from the catalogue: {products}.\
        You should keep the user profile in mind while answering the questions.\
        Only include data from {products} to write summary of the recommedation.\
        Start with a brief summary of each insurance in the following format, in decreasing order of Annual Premium of insurance:
        1. <Insurance Name> : <Major features of the insurance>, <Annual Premium in Rs>
        2. <Insurance Name> : <Major features of the insurance>, <Annual Premium in Rs>

        """
        conversation = [{"role": "system", "content": system_message }]
        return conversation