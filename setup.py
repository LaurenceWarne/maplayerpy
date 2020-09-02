from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    "numpy==1.19.1",
    "typeguard==2.9.1",
]

TEST_REQUIRES = [
    "tox",
    "opencv-python"
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
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "test": TEST_REQUIRES
    },
    zip_safe=False,
)
