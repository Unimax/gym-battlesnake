import os
import subprocess

from setuptools import setup

setup(
    name="gym_battlesnake",
    version="0.0.1",
    author="Arthur Firmino",
    author_email="arthur.p.v.firmino@gmail.com",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Unimax/gym-battlesnake",
    packages=["gym_battlesnake"],
    install_requires=[
        'gym',
        'numpy',
        'stable-baselines',
    ],
    zip_safe=False,
)
