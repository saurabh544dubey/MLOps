## Set up the GitHub
1. New Environment : Create and activate an environment first
2. Initialize and setup the repository
3. Create .gitignore in repository
4. Create setup.py -- It'll be responsible for creating my ML Application as a package.
5. Create folder `src` and under it file `__init__.py`: This can be imported like libraries. All the project development inside this folder.
6. Create requirements.txt -- store packages to be used. At last, we'll mention `-e .` which will automatically trigger setup.py file.
Comment down `-e .` after it is executed so that when we install more libraries later on, my package will not build again and again.

#### To install Libraries
- `pip install -r requiremnts.txt`

## Creating Project Structure
**Components Folder**
- Create a folder inside src called `components` and a file `__init__.py` inside the folder.
- In components, there will going to be all the modules that we are going to create like `Data Ingestion`,`Data Transformation`,etc.
- Create `data_ingestion.py`,`data_transformation.py`,`model_trainer.py` inside components folder.
- In these files, I'll write code inside these files only.

**Pipeline Folder**
- Create a folder called `pipeline` inside src.
- Create 2 files inside the folder `train_pipeline.py` and `predic_pipeline.py`.
- I'll call components inside these pipeline files.
- I will create another file inside pipeline `__init__.py` so that I can import this.

<br>
- Create these files inside src folder
    1. `logger.py` : For Loggging
    2. `exception.py` : For Exception handling purpose
    3. `utils.py` : For writing functionalities which will be used in the entire application like `save_model` function.


### Exception
- For Exception Handling, we will use `sys` library.
- I will make my own `error message` and `CustomException` class.
- Then when I raise exception, my error message will print with details.

### Logging
- It is used for the purpose that any execution that probably happens, we should be able to log all the information and everything in some files so that we will be able to track.
- Even if there is some errors, it'll try to log that into the text file.
- A file inside a folder will be created with information in the specified format.


## EDA and Model Training
- Create a folder `Notebook` and inside create 2 ipynb files i.e EDA and Model Training.
- I will do the EDA and Model Training here because it is easy to do it in Jupyter notebook.
- I will store my data in this `Notebook` folder.

- After doing all these, I will go into my src folder and do Modular coding by writing functions.
- I will do all these again in the respective files I created under src.

## Data Ingestion
- Reading the Data from some specific source.
- Then we'll train_test_split the data.
- Then I save the data into artifacts folder and return the paths from the class so as to be used in Data Transformation.
- After executing all this, add `.artifacts` in gitignore file

## Data Transformation
- Mean aim is to do Feature Engineering, Data Cleaning, converting categorical Features and so on...
- I did this in Jupyter. Now I'll modular code it in form of classes and functions in my Data Transformation file.
- We will make our `save_object` function in `utils.py` beccause we will be using it in others too.
- We'll use `dill` library to save the model.

## Model Training
- Create a class to train the models.
- We'll try every model and select the model which is giving us the best results.
- We will evaluate models by crreating a function in `utils.py`.
- We are storing it in a dictionary and returning the model with best score.
- Then we are saving that model.

## Hyperparameter tuning
- We will do this in the same model trainer file.
- We can also do it in another file.
- We'll specify the parameters in the model trainer and create a parameter in evaluate model in `utils.py`.
- Then we write the code to train on hyperparameters and selecting the best one.

## Prediction pipeline
- We will make it using Flask web app.
- User will give us data, then we have 2 pickle files i.e  `preprocessor` and `model` and we use them to generate predictions on user data.
- Create `app.py` outside of each folder.
- Create a folder `templates` to store html templates.
- Prediction part will be done in `predict_pipeline.py` file.
- I get Data from my user and then convert it into DataFrame in `predict_pipeline.py` file.

## Deployment using CI/CD
- Here I am going to be doing in AWS.
- We need to make some configuration changes.
- We have to setup 2 important configurations whenever we are working with `elastic beanstalk` which is a kind of instance which is provided to deploy entire application.
- Create a folder `.ebextensions` and inside that create a file `python.config`
- The `python.config` file is mainly to tell the `elastic beanstalk` the entry point of the application.
- Create a file `application.py` and copy all the code of `app.py` and remove `debug=True` from the last line of code if any.
- This is just for the deployment purpose only.
- Now, commit and push the code.