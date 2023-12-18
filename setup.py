from setuptools import find_packages , setup
from typing import List

hyphen_e_dot = '-e .'

 # given our file path in str type its return type would be list of strings
def get_requirements(file_path : str)-> List[str] :
    '''
    this function will return the list of requirements
    '''          
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        # /n comes on new line due to readlines and we have to remove it 
        requirements = [req.replace('\n','') for req in requirements]

    if hyphen_e_dot in requirements :
        requirements.remove(hyphen_e_dot)

    return requirements    

setup(
name = 'mlproject',
version='0.0.1',
author= 'siddhesh',
author_email= 'siddheshshinde1000@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt') 
)