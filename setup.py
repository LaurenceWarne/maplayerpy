from setuptools import setup, find_packages


with open("requirements.txt") as f:
    dependencies = f.readlines()

setup(
    name="maplayerpy",
    packages=find_packages(),
    include_package_data=True,
    test_suite="maplayerpy.tests",
    python_requires='>=3.6',
    url="",
    version="0.1",
    author="Laurence Warne",
    license="MIT",
    install_requires=dependencies,
    zip_safe=False
)
