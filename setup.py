'''
The setup.py is an essential part of packaging and distributing python projects. It is used by setuptools (or)
(distutils in older Python versions) to define teh configuration of your project, scuh as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines =  file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
         print("requirements.txt not found")
    
    return requirement_list

setup(
    name="MD-NetworkSecurity",
     version="0.0.1",
     author="Adegoke M.D",
     author_email="aadegokemuideen@yahoo.com",
     packages=find_packages(),
     install_requires=get_requirements()
)

if __name__ == "__main__":
    print(get_requirements())
