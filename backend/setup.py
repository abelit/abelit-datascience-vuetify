# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2020/03/21 08:31:18
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from setuptools import setup

setup(
    name='DataScience',
    version='1.0',
    long_description=__doc__,
    packages=['datascience'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
