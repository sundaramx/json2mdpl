import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2mdpl",
    version="1.0.0",
    author="Sundar Rajan",
    description="json2mdpl is a python library for converting json to md ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sundaramx/json2mdpl",
    packages=setuptools.find_packages(),
    entry_points={
        "scripts": [
            "json2mdpl = json2mdpl:init:main"
        ]
    },
    classifiers=[
        "Language :: Python :: 3.x",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.x',
)
