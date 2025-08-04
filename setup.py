from setuptools import setup, find_packages

setup(
    name="ben10-cli",
    version="1.00",

    install_requires=[
        "prettytable",
        "beautifulsoup4",
        "requests",
        "argparse"
        ],

    scripts=[
        "ben10-cli",
    ]
)
