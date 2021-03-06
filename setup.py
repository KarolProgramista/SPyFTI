from setuptools import setup, find_packages

config = {
    'description': 'SPyFT is Simple Python File Transceiver which can easily transfer files',
    'author': 'Karol Konat',
    'url': 'https://github.com/KarolProgramista/SPyFT',
    'download_url': 'https://github.com/KarolProgramista/SPyFT',
    'author_mail': 'konatkarol@gmail.com',
    'version': '1.0',
    'install_requires': [],
    'packages': find_packages(),
    'scripts': [],
    'name': 'SPyFT',
    'classifiers': [

        "Programming Language :: Python :: 3",

        "Operating System :: OS Independent"],

    'python_requires': '>=3.6'
}

setup(**config)
