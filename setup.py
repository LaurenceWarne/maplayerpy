from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    "numpy==1.19.1",
    "typeguard==2.9.1",
    "perlin-numpy @ git+https://github.com/pvigier/perlin-numpy/",
]

TEST_REQUIRES = ["pytest"]

setup(
    name="maplayerpy",
    packages=find_packages(),
    include_package_data=True,
    test_suite="tests",
    python_requires=">=3.6",
    url="https://github.com/LaurenceWarne/maplayerpy",
    version="0.1",
    author="Laurence Warne",
    license="MIT",
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES},
    zip_safe=False,
)
