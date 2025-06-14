from setuptools import setup, find_packages
from typing import List

def get_requirements(path : str) -> List[str]:
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
    requirements = [req.replace("\n", "") for req in requirements if not req.startswith("-e")]

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="abhishek roy",
    author_email="aroy1856@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)