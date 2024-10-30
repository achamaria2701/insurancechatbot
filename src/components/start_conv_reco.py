from src.pipeline.logger import logging

class ConvRecommendation():

    def __init__(self):
        pass

    def initialize_conv_reco(self, products):
        logging.info("Initializing reccomendation conversation")
        
        system_message = f"""
        You are an intelligent insurance expert and you are tasked with the objective to \
        solve the user queries about any product from the catalogue: {products}.\
        You should keep the user profile in mind while answering the questions.\
        Only include data from {products} to write summary of the recommedation.\
        Start by saying that here are the insurnace recommendations based on your requirements.\
        Then with a brief summary of each insurance in the following format, in decreasing order of Annual Premium of insurance:
        1. <Insurance Name> : <Major features of the insurance>, <Annual Premium in Rs>
        2. <Insurance Name> : <Major features of the insurance>, <Annual Premium in Rs>

        """
        conversation = [{"role": "system", "content": system_message }]
        return conversation