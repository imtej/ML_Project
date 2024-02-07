from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function is going to return the list of all requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        


setup(
    name = 'ML_Project',
    version='0.0.1',
    auther ='RAVI TEJ',
    author_email='ravitej.j11@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')


)