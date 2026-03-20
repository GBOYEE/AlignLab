from setuptools import setup, find_packages

setup(
    name="alignlab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "alignlab=alignlab.cli:main",
        ],
    },
    python_requires=">=3.8",
)