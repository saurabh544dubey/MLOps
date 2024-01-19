import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ### By using this decorator, I can directly specify variables without writing __init__ in class


from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer


### We have to make a class in which we will be specifying the paths where to save the extracted data. Raw Data,Train Data,Test Data

### Because we're just defining variables, therefore I am using dataclass
@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join("artifacts","train.csv")   ### Path of file --> artifacts/train.csv
    test_data_path : str = os.path.join("artifacts","test.csv")   ### Path of file --> artifacts/test.csv
    raw_data_path : str = os.path.join("artifacts","data.csv")   ### Path of file --> artifacts/data.csv
    

    
### Because I have to define methods in the class, I am using __init__ inside the class instead of dataclass
class DataIngestion:
    def __init__(self):
        ### Making object of DataIngestionConfig inside.
        self.ingestion_config=DataIngestionConfig()   ### Variable stores in self.ingestion_config
     
    ### We'll write code to read from the Databases  
    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method")
        try:
            ### Reading the data
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the Dataset in the dataframe")
            
            ### Creating directories
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            ## Saving raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test Split initiated")
            
            ## Train Test Split
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            ## Saving the train and test set
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion is completed")
            
            ### I will be returning the path of Datasets so that it will be used in Data Transformation
            return self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
             
        except Exception as e:
            raise CustomException(e,sys)
        
        
### Initiating Data Ingestion
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
    
## Terminal - python src/components/data_ingestion.py