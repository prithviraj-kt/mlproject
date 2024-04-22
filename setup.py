from setuptools import find_packages, setup
from typing import List

CONST = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if CONST in requirements:
            requirements.remove(CONST)
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author="Prithviraj",
    author_email="prithvirajtagadinamani@gmail.com",
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)