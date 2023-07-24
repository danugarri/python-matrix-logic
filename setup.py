from setuptools import setup, find_packages

setup(
    name="Python Matrix logic",
    version="1.0.0",
    description="This is a python package to handle multidimensional arrays with its corresponding unit tests with unittest",
    author="Daniel Garrido",
    packages=find_packages(),
    # scripts
    entry_points={
        "console_scripts": [
            # Main script
            "generate-matrix = python.__init__:generate_matrix",
        ],
    },
)
