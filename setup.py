from setuptools import find_packages, setup
from typing import List

hyphen_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    '''
    This function reads all the requirements from given file line by line
    and returns the list of those requiirements.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hyphen_E_DOT in requirements:
            requirements.remove(hyphen_E_DOT)

    return requirements

setup(
    name = 'ML Project'
    version = '0.0.1'
    author = 'Manisha Dhanuka'
    packages = find_packages(),
    install_requires = get_requirements(requirements.txt)
)