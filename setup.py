from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mtkdata",
    version="0.1",
    author="jlam",
    author_email="joey.cm.lam@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown; charset=UTF-8",
    url="https://github.com/joeycmlam/mktdata",
    packages=find_packages(),
    install_requires=[
        "behave",
        "requests",
        "flask",
        "flask-restful",
        "flask-cors"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
