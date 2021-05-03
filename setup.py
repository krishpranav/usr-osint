#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='usr-osint',
    version="1.3.4",
    packages=find_packages(),
    author="krishpranav",
    author_email="krisna.pranav@gmail.com",
    install_requires=["pwnedpasswords", "requests", "PyInquirer", "jinja2", "argparse"],
    description="usr-osint is an OSINT tool that allows you to find potential profiles of a person on social networks, as well as their email addresses and shows you the data leak of the found emails.",
    include_package_data=True,
    url='https://github.com/krishpranav/usr-osint',
    classifiers=[
        "Programming Language :: Python",
    ],
    license='MIT'
)