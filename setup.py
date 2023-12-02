from setuptools import setup

setup(
    name="pyMooGoldApi",
    version="1.0",
    python_requires=">=3.8",
    packages=["MooGold"],
    install_requires=["aiohttp>=3.7.1,<4.0.0a0"],
    url="https://github.com/dzmuh97/pyMooGoldApi",
    author="Ilya Dz",
    author_email="i.dzmuh@gmail.com",
    keywords="moogold, api, async",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
