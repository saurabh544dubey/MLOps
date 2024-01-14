## Set up the GitHub
1. New Environment : Create and activate an environment first
2. Initialize and setup the repository
3. Create .gitignore in repository
4. Create setup.py -- It'll be responsible for creating my ML Application as a package.
5. Create folder `src` and under it file `__init__.py`: This can be imported like libraries. All the project development inside this folder.
6. Create requirements.txt -- store packages to be used. At last, we'll mention `-e .` which will automatically trigger setup.py file.

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