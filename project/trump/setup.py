#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='trump',
      url='',
      author='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      version='0.0.1',
      install_requires=[
          'numpy==1.11.0',
          'scipy==0.19.1',
          'pandas==0.20.3',
          'pytest==3.2.2',
          'docopt==0.6.2',
          'nltk==3.2.5',
          'profanity==1.1',
          'emoji==0.4.5'
      ],
      include_package_data=True,
      zip_safe=False)
