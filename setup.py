# coding=utf-8
from setuptools import setup

setup(
    name="echo-server",
    description="Python 401 http echo http-server",
    version=0.1,
    author= 'David Flegal',
    author_email='flegal.david@gmail.com',
    license="MIT",
    py_modules=["client", "server"],
    package_dir={},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)