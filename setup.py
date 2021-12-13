import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="logparser",
    version="1.0.0",
    py_modules=['logparser'],
    author="Diego Noceda",
    author_email="dfynar@gmail.com",
    description="Python CLI application that helps parsing logs of various kinds.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Fynardo/logparser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
    ],
    python_requires='>=3.8.5',
)


