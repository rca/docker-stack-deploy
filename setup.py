#!/usr/bin/env python
import os

from setuptools import setup

entry_points = {
    'console_scripts': [
        # 'bar = testpackage.console_scripts:bar',
    ],
}

scripts = [
    'scripts/docker-stack-deploy',
]

setup(
    name='docker-stack-deploy',
    url='https://github.com/rca/docker-stack-deploy',
    author='Roberto Aguilar',
    author_email='roberto.c.aguilar@gmail.com',
    version='0.0.0',
    # package_dir={'': 'src'},
    packages=[],
    scripts=scripts,
    entry_points=entry_points,
    install_requires=[
        'sh',
    ]
)
