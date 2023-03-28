# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='filelock',
    version='3.12.1',
    description='A platform independent file lock.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
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
            'furo>=2023.5.20',
            'sphinx-autodoc-typehints!=1.23.4,>=1.23',
            'sphinx>=7.0.1',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.2.7',
            'diff-cover>=7.5',
            'pytest-cov>=4.1',
            'pytest-mock>=3.10',
            'pytest-timeout>=2.1',
            'pytest>=7.3.1',
        ],
    },
    packages=[
        'filelock',
    ],
    package_dir={'': 'src'},
)
