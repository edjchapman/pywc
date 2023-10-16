import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setuptools.setup(
    name="pywc",
    version="0.0.5",
    author="Ed Chapman",
    author_email="ed@edchapman.co.uk",
    license="MIT",
    description="Python implementation of the UNIX wc (Word Count) utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edjchapman/pywc",
    py_modules=["pywc"],
    packages=setuptools.find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "pywc = pywc.cli:wc",
        ],
    },
)
