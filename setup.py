from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    '''
    This function will return the list of
    requirements specified in filepath
    '''
    requirements = []
    with open(filepath, 'r') as f:
        requirements= f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='ML-Project',
version='0.0.1',
author='BangLe - repusemem',
author_email="bangle.lcb@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)
