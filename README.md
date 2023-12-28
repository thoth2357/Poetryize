[![Tests](https://github.com/thoth2357/Poetryize/actions/workflows/python-app.yml/badge.svg)](https://github.com/thoth2357/Poetryize/actions/workflows/python-app.yml) [![Coverage Status](https://coveralls.io/repos/github/thoth2357/Poetryize/badge.svg?branch=main)](https://coveralls.io/github/thoth2357/Poetryize?branch=main) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Poetryize)

# Poetryize

Poetryize is a command-line tool built with Typer that facilitates the conversion of requirements.txt files into pyproject.toml files. This allows seamless integration with Poetry, a dependency manager for Python projects. If you've ever found yourself wanting to use Poetry for dependency management but stuck with a project that uses requirements.txt, Poetryize is here to help.

## Features

- **Seamless Conversion**: Poetryize effortlessly transforms requirements.txt files into pyproject.toml files compatible with Poetry.
- **Dependency Initialization**: Poetryize automatically initializes Poetry if a pyproject.toml file is not found in the project, streamlining the conversion process.
- **Error Handling**: Poetryize includes error-handling mechanisms to address issues with the specified requirements file, providing informative messages to guide users.
- **Versatile Support**: Poetryize supports a range of requirements.txt formats, including:
  - `package==version`
  - `package>=version`
  - `package<=version`
  - `package~=version`
  - `package`


## Installation

```bash
  pip install poetryize
```

## Example/Usage
#### 1. Using Poetryize on project folder with requirements.txt file
```
├── create_db.py
├── database.py
├── main.py
├── models.py
├── __pycache__
│   ├── database.cpython-310.pyc
│   ├── main.cpython-310.pyc
│   └── models.cpython-310.pyc
├── requirements.txt
└── test_main.http
```
- Run poetryize on the project folder, while in the same directory as the requirements.txt file
```bash
  poetryize
```

-

**Note**: Using Poetryize without any requirement.txt path argument would automatically use the requirements.txt file in the project folder.

#### 2. Using Poetryize on a project with a requirements.txt file in a different folder
``` bash
  poetryize /path/to/requirements.txt
```


## Demo
<video src='https://github.com/thoth2357/Poetryize/assets/98170427/b2a72dad-c484-4cbf-b4c4-2923eb4be59a' height=50></video>

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
