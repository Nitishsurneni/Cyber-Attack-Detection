from setuptools import find_packages, setup
from typing import List 
hypen_e = '-e .'
def remove_hyphen_e(requirements: List[str]) -> List[str]:
    """
    This function removes the '-e .' entry from the requirements list.
    """
    if hypen_e in requirements:
        requirements.remove(hypen_e)
    return requirements

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements from a file and returns a list of requirements.
    It also removes the '-e .' entry if it exists.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements]
    return remove_hyphen_e(requirements)

setup(
    name='cybersecurity',
    version='0.1',
    description='A package for cybersecurity tools and utilities',
    author='Siva Nitish Surneni',
    author_email='nitishsurneni@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt'),
)