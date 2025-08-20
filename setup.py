# Flake8: noqa

from pathlib import Path
from setuptools import setup, find_packages
import os

NAME = "package_etl"
VERSION = ""

if not VERSION:
    VERSION = os.environ.get("VERSION")

DESCRIPTION = """Python module for package_etl"""
KEYWORDS = ["Momar", "package_etl"]

URL = "https://github.com/Momarsallgueye/package_data"
LICENSE = "NO LICENSE"

# http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Plugins",
    "Intended Audience :: Developers",
    "License :: Other/Proprietary License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries",
]

AUTHOR = "Momar Sall GUEYE"
AUTHOR_EMAIL = "sallmomargueye89@gmail.com"
MAINTAINER = "Momar Sall GUEYE"
MAINTAINER_EMAIL = "sallmomargueye89@gmail.com"

PYTHON_REQUIRES = ">=3.9"

# Insert here the package dependencies
REQUIRES = [
    'pandas',
    'numpy'
    
]

EXTRAS_REQUIRE = {}


# Get the long description from the README file
MODULE_DIR = Path(__file__).parent
with open(MODULE_DIR / "README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=KEYWORDS,

    url=URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,

    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,

    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,

    packages=find_packages(),
    include_package_data=False
)
