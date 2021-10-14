<<<<<<< HEAD
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    author="Angelos Anagnostopoulos",
    author_email="angelosanag@protonmail.com",
    description="A utility for backing up PostgreSQL databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AngelosAnagnostopoulos/pgbackup",
    packages=find_packages("src")
        )
=======
from setuptools import setup, find_packages

with open('README.rst', encoding = 'utf-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Angelos Anagnostopoulos',
    author_email='angelosanag@protonmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts':'hr=hr.cli:main'
    }
)
>>>>>>> 3dd6d3d (Done)

