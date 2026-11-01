from setuptools import setup

setup(
    name='filelock',
    version='4.2.5',
    description='A platform independent file lock.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
    ],
    packages=[
        'filelock',
        'filelock._soft_rw',
    ],
    package_dir={'': 'src'},
)
