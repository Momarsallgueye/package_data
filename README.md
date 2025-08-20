# Module package_etl

## Development of the project

When you are develloping your application you have to work on branch dev, change the directory with the name "python-dependency-template" with you project name.  [In the setup file](setup.py) , change the NAME value with your project name 

```python
NAME = "package_etl"
```

## Installation

<br/>

```bash
# Create virtual env
python -m venv ./venv

# Activate virtual environment
./venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependancies
pip install .

# Or for dev. environment
pip install -r dev-requirements.txt
```
<br/>

## Deployment of the project

When you need to deploy your project, please be sure to have the right NAME of your project in the setup file. Change the [VERSION](VERSION) file with a new version. 
The first digit of VERSION represent major update, the second digit represent an epic, and the last digit represent feature and hotfix.



## Tests

Tests require devlopment environment activated.

```bash
# Execute all tests
pytest

# Execute specific test
pytest -k <test_name>

# Execute test with more verbose
pytest -v

# Execute test and capture std ouput to be re-print
pytest -rP

```

Resources required for tests are stored in directory : `./tests/data/<test_file_name>/`

<br/>
