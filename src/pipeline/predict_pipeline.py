import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    """This class will predict based on the data given by user 
    """
    
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e,sys)
        
          
class CustomData:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        ### These values will be coming from my Web App provided by user
        self.gender=gender,
        self.race_ethnicity=race_ethnicity,
        self.parental_level_of_education=parental_level_of_education,
        self.lunch=lunch,
        self.test_preparation_course=test_preparation_course,
        self.reading_score=reading_score,
        self.writing_score=writing_score
        
    def get_data_as_data_frame(self):
        """This function will convert our user data into a DataFrame

        Returns:
            _type_: pandas DataFrame
        """
        
        try:
            custom_data_input_dict={
                "gender":self.gender,
                "race_ethnicity":self.race_ethnicity,
                "parental_level_of_education":self.parental_level_of_education,
                "lunch":self.lunch,
                "test_preparation_course":self.test_preparation_course,
                "reading_score":self.reading_score,
                "writing_score":self.writing_score
            }
            
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)