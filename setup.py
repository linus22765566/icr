from setuptools import setup, find_packages

setup(
    name="icr-kaggle",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    description="icr kaggle",
    install_requires=[
        "pytorch-model-utils @ git+https://github.com/bhbbbbb/pytorch-model-utils",
    ],
)
