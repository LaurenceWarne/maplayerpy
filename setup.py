from setuptools import find_packages, setup

DEPENDENCIES = [
    "certifi==2020.6.20",
    "cycler==0.10.0",
    "kiwisolver==1.2.0",
    "matplotlib==3.3.1",
    "numpy==1.19.1",
    "perlin-numpy @ git+https://github.com/laurencewarne/perlin-numpy@155cf9e211cda63891707d374d18ebac8eddd398",
    "Pillow==7.2.0",
    "pyparsing==2.4.7",
    "python-dateutil==2.8.1",
    "six==1.15.0",
    "typeguard==2.9.1",
]

setup(
    name="maplayerpy",
    packages=find_packages(),
    include_package_data=True,
    test_suite="tests",
    python_requires=">=3.6",
    url="",
    version="0.1",
    author="Laurence Warne",
    license="MIT",
    install_requires=DEPENDENCIES,
    zip_safe=False,
)
