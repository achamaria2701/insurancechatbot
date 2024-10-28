import pandas as pd
import os

class DataIngestion:

    def __init__(self):
        self.data_path = os.path.join('artifact','health_insurance_dataset.csv')

    def initiate_data_ingestion(self):
        df = pd.read_csv(self.data_path)
        return df