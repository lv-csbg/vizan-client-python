from io import open
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'vizan_client/__init__.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.1.0'

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read()

REQUIRES = ['cobra', 'pandas', 'requests']

setup(
    name='vizan-client-python',
    version=version,
    description='A web client to VizAn REST server, global or local.',
    long_description=LONG_DESC,
    author='Rudolfs Petrovs',
    author_email='rudolfs.petrovs@glu.lv',
    maintainer='Rudolfs Petrovs',
    maintainer_email='rudolfs.petrovs@glu.lv',
    url='https://github.com/lv-csbg/vizan-client-python',
    license='GPLv3',

    keywords='VizAn FBA FVA',

    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: FSF Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(exclude=['docs', 'tests']),
)
