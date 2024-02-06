# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='filelock',
    version='3.15.1',
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
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
    ],
    extras_require={
        'docs': [
            'furo>=2023.9.10',
            'sphinx-autodoc-typehints!=1.23.4,>=1.25.2',
            'sphinx>=7.2.6',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.3.2',
            'diff-cover>=8.0.1',
            'pytest-asyncio>=0.21',
            'pytest-cov>=4.1',
            'pytest-mock>=3.12',
            'pytest-timeout>=2.2',
            'pytest>=7.4.3',
        ],
        'typing': [
            'typing-extensions>=4.8; python_version < "3.11"',
        ],
    },
    packages=[
        'filelock',
    ],
    package_dir={'': 'src'},
)
