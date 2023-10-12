# this setup.py will be responsible to built my ML application as a package and deploy in PyPI(python package index)
# so that anybody can do the instllation and anybody can use it

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name ='student_performance_indicator',
    version ='0.0.1',
    author ='keerthi',
    author_email= 'keerthyy97@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']
    install_requires = get_requirements('requirements.txt')
)