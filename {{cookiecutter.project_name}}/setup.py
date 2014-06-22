# coding: utf-8
from setuptools import setup

setup(
    name='{{ project_name }}',
    version='0.1.0',

    scripts=['scripts/manage.py'],
    entry_points = {
        'console_scripts': [
            '{{ project_name }} = manage:main',
        ],
    }
)
