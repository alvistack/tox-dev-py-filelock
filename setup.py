# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='filelock',
    version='3.10.3',
    description='A platform independent file lock.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
    ],
    extras_require={
        'docs': [
            'furo>=2022.12.7',
            'sphinx-autodoc-typehints!=1.23.4,>=1.22',
            'sphinx>=6.1.3',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.2.2',
            'pytest-cov>=4',
            'pytest-timeout>=2.1',
            'pytest>=7.2.2',
        ],
    },
    packages=[
        'filelock',
    ],
    package_dir={'': 'src'},
)
