# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top

import re
import setuptools


def get_package_dir():
    pkg_dir = {}
    return pkg_dir


def get_install_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    return reqs


def get_picsocket_version():
    with open("picsocket/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setuptools.setup(
    name="picsocket",
    version=get_picsocket_version(),
    author="Coder.AN",
    url="https://github.com/BestAnHongjun/PicSocket",
    package_dir=get_package_dir(),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=get_install_requirements(),
    setup_requires=["wheel"],  # avoid building error when pip is not updated
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,  # include files in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3", "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    project_urls={
        "Documentation": "https://github.com/BestAnHongjun/PicSocket",
        "Source": "https://github.com/BestAnHongjun/PicSocket",
        "Tracker": "",
    },
)
