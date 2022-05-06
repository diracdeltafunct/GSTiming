"""
Copyright 2015 BrightSpec
"""
from setuptools import find_packages
from setuptools import setup


if __name__ == "__main__":
    # we only use a setup.py file so we can install Edgar into a virtual environment
    # in editable mode
    setup(
        name="gstiming",
        version="DEV",  # actual installer version is obtained later
        author="BrightSpec",
        author_email="support@brightspec.com",
        url="https://brightspec.com",
        packages=find_packages(include=["gstiming*"]),
        entry_points={"console_scripts": []},
        # we use requirements.txt to declare dependencies
        install_requires=[],
        tests_require=[],
        setup_requires=[],
        extras_require={},
        zip_safe=False,
        include_package_data=True,
    )
