# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

PY3 = sys.version_info[0] == 3

install_requires = [
        "setuptools",
        "robotframework-selenium2library",
        "robotframework-databaselibrary",
        "psycopg2",
    ]

if PY3:
    install_requires.append('robotframework-python3 >= 2.6.0')
else:
    install_requires.append('robotframework >= 2.6.0')

setup(
    name="robotframework-odoo",
    version='0.0.1',
    description="Robot Framework keyword library for Odoo",
    long_description=(open("README.rst").read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="",
    author="Raphaël Valyi",
    author_email="raphael.valyi@akretion.com",
    url="https://github.com/akretion/odoo-robot-framework",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
