# coding: utf-8
from setuptools import setup

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1.0',

    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_name }} = manage:main',
        ],
    }
)
