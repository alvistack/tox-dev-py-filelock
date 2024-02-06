# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='filelock',
    version='3.16.0',
    description='A platform independent file lock.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
    ],
    extras_require={
        'docs': [
            'furo>=2024.8.6',
            'sphinx-autodoc-typehints!=1.23.4,>=2.4',
            'sphinx>=8.0.2',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.6.1',
            'diff-cover>=9.1.1',
            'pytest-asyncio>=0.24',
            'pytest-cov>=5',
            'pytest-mock>=3.14',
            'pytest-timeout>=2.3.1',
            'pytest>=8.3.2',
            'virtualenv>=20.26.3',
        ],
        'typing': [
            'typing-extensions>=4.12.2; python_version < "3.11"',
        ],
    },
    packages=[
        'filelock',
    ],
    package_dir={'': 'src'},
)
