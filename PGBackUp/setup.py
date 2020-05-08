from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Szymon Czajka',
    author_email="A utility for backing up PostgreSQL databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SzymonCzajka/python-tools/pgbackup',
    packages=find_packages('scr')
)
