from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

class DataPipeline:

    def __init__(self):
        pass

    def get_data(self):
        data_obj = DataIngestion()
        laptop_df = data_obj.initiate_data_ingestion()

        transform_obj = DataTransformation()
        transformed_df = transform_obj.preprocess_laptop_data(laptop_df)
        return transformed_df