#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import edbo_connector

setup(
    name=edbo_connector.__name__,
    version=edbo_connector.__version__,
    author=edbo_connector.__author__,
    author_email=edbo_connector.__email__,
    maintainer=edbo_connector.__author__,
    maintainer_email=edbo_connector.__email__,
    url='https://github.com/EldarAliiev/python-edbo-connector',
    download_url='https://github.com/EldarAliiev/python-edbo-connector.git',
    license=edbo_connector.__license__,
    description='edbo_connector',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    install_requires=[
        'requests==2.18.3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: %s License' % edbo_connector.__license__,
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
    ],
    keywords=[
        'EDBO',
        'connector',
        'RESTful API',
        'EDBO client',
    ],
    test_suite='tests',
    zip_safe=False,
    include_package_data=True
)
