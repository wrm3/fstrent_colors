from setuptools import setup, find_packages

setup(
    name="fstrent_colors",
    version="0.1.2",
    author="Warren R Martel III",
    author_email="wrmartel3@gmail.com",
    description="enhanced colors options for terminal output",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wrm3/fstrent_colors",
    py_modules=[
        "fstrent_colors",
        "fstrent_colors_base",
        "fstrent_colors_on_black",
        "fstrent_colors_on_white",
        "fstrent_colors_on_gray",
        "fstrent_colors_on_blue",
        "fstrent_colors_on_cyan",
        "fstrent_colors_on_green",
        "fstrent_colors_on_magenta",
        "fstrent_colors_on_red",
        "fstrent_colors_on_yellow"
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