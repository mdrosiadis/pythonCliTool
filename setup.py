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
