from setuptools import setup, find_packages


long_description = open('README.md').read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.2.0'

setup(
    name='ontoutils',
    version=version,
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ccb-hms/ontoutils',
    description='Utilities to write an ontology class hierarchy as a Newick tree or as a table.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rafael Goncalves, Center for Computational Biomedicine, Harvard Medical School',
    author_email='rafael_goncalves@hms.harvard.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ]
)
