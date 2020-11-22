import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2mdpl",
    version=str(),
    author="Sundar Rajan",
    description="json2mdpl is a python library for converting json to md ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={
        "scripts": [
            "json2mdpl = json2mdpl:init:main"
        ]
    },
    classifiers=[
        "Language :: Python :: 3.x",
        "License :: MIT License",
    ],
    python_requires='>=3.x',
)
