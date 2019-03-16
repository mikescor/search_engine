from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='search_engine',
    description='Indexing of documents using Python',
    url='https://github.com/mikescor/search_engine',
    install_requires=requirements,
    zip_safe=False
)
