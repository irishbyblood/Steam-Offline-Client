#!/usr/bin/env python3
"""
Setup script for Steam Offline Client
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="steam-offline-client",
    version="1.0.0",
    author="irishbyblood",
    description="Your steam games Downloader for mobile download offline non streaming gameplay",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irishbyblood/Steam-Offline-Client",
    py_modules=["steam_offline_client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "steam-offline-client=steam_offline_client:main",
        ],
    },
)
