import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.1.0"

REPO_NAME = "house-price-instelligence-system"
AUTHOR_NAME = "Gautam Mishra"
SRC_REPO = 'src'
AUTHOR_EMAIL = 'g20autammishra1234@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='An ML pipeline for Bengaluru house price prediction with MLOps and an analytics layer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/GautamMishra20/house-price-intelligence-system",
    project_urls={
        'Bug Tracker' : f"https://github.com/GautamMishra20/house-price-intelligence-system/issues"
    },
    packages=find_packages(),
    python_requires=">=3.9",
)

