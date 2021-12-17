#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "tap-kustomer==1.0.2",
    "airbyte-cdk",
]

TEST_REQUIREMENTS = [
    "pytest~=6.1",
    "source-acceptance-test",
]

setup(
    name="source_kustomer_singer",
    description="Source implementation for Kustomer, built on the Singer tap implementation.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
