from setuptools import find_packages, setup

with open("requirements.txt") as f:
    dependencies = f.readlines()

setup(
    name="maplayerpy",
    packages=find_packages(),
    include_package_data=True,
    test_suite="tests",
    python_requires='>=3.6',
    url="",
    version="0.1",
    author="Laurence Warne",
    license="MIT",
    install_requires=dependencies,
    zip_safe=False
)
