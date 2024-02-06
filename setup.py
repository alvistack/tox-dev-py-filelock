# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='filelock',
    version='3.12.3',
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
    install_requires=[
        'typing-extensions>=4.7.1; python_version < "3.11"',
    ],
    extras_require={
        'docs': [
            'furo>=2023.7.26',
            'sphinx-autodoc-typehints!=1.23.4,>=1.24',
            'sphinx>=7.1.2',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.3',
            'diff-cover>=7.7',
            'pytest-cov>=4.1',
            'pytest-mock>=3.11.1',
            'pytest-timeout>=2.1',
            'pytest>=7.4',
        ],
    },
    packages=[
        'filelock',
    ],
    package_dir={'': 'src'},
)
