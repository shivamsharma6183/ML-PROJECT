from setuptools import find_packages,setup
from typing import  List
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return tje list of requirement 
    '''
    requirement = []

    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements = [req.replace('\nf',"") for req in requirement]
    return requirements




setup(
name='mlproject',
version='0.0.1',
author = 'shivam',
author_email = 'shivamsharma6183@gmail.com',
packages = find_packages(),
install_requires  = get_requirement('requirement.txt')



)

