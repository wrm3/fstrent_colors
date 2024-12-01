# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="fstrent_colors",
    version="1.0.1",
    author="Warren R Martel III",
    author_email="wrmartel3@gmail.com",
    description="enhanced colors options for terminal output",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wrm3/fstrent_colors",
    py_modules=[
        "fstrent_colors"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "colorama",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
            "bump2version>=1.0",
            "build",
            "twine",
        ],
    },
) 