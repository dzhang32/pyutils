import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyutils",
    version="0.0.2",
    author="David Zhang",
    author_email="dyzhang32@gmail.com",
    description="A home for my commonly-used python utility functions",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/dzhang32/pyutils",
    project_urls={
        "Bug Tracker": "https://github.com/dzhang32/pyutils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
