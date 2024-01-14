from setuptools import find_packages,setup
from typing import List

HYPHER_E_DOT="-e ."
### It'll fetch the libraries from requirements.txt file
def get_requirements(file_path:str)->list[str]:
    """This function will return the list of requirements

    Args:
        file_path (str): This is the path of the requirements file

    Returns:
        list[str]: It is returning a list of all packages to be installed  
    """

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        ### When we read lines this way, it'll also read \n, we have to replace it with  ""
        requirements=[req.replace("\n","") for req in requirements]
        
        ### Because -e . is also read which triggers setup.py, we have to remove it from the installing list
        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)
            
    return requirements

### This is basically information about Project
setup(
    name="mlproject",
    version="0.0.1",
    author="Saurabh",
    author_email="Saurabhbcp2122@gmail.com",
    packages=find_packages(),   ## It'll consider src as a package itself
    install_requires=get_requirements("requirements.txt")
)

