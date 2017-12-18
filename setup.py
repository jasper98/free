#!/usr/bin/env python
# coding: utf8

from setuptools import setup

import free

setup(
    name='macos-free',
    version=free.__version__,
    keywords=['memory', 'macos', 'linux', 'free'],
    description='Memory usage for macos, an alternative to free command.',
    author='cls1991',
    author_email='tzk19910406@hotmail.com',
    url='https://github.com/cls1991/free',
    py_modules=['free'],
    install_requires=[
        'click>=6.7',
        'prettytable>=0.7.2',
        'sh>=1.12.14'
    ],
    license='Apache 2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': ['free = free:main']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: MacOS'
    ]
)
