from setuptools import setup

setup(
    name='Data Science',
    version='1.0',
    long_description=__doc__,
    packages=['datascience'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
