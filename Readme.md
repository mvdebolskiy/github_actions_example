# Pytest

Python testing framework to simplify testing of your code. Detailed instructions on how it is used (and installed) can 
be found here: [Pytest Instructions](https://realpython.com/pytest-python-testing/) or [Pytest Documentation](https://docs.pytest.org/en/latest/contents.html).

The test scripts are in the directory [pytest](pytest). pytest will run all files of the form `test_*.py` or `*_test.py`
in the current directory and its subdirectories and in these files all functions with the prefix `test` will be run.

To run all tests:
```bash
python -m pytest
```

# Python Linter

Linters will check your code syntax and provide instructions on how to clean it. They can detect your Python code 
mistakes, notice invalid code patterns and find elements that do not follow your conventions. Python linters have a 
number of advantages, such as: 

* Linting makes you a better developer by helping you write better code (checking against coding standards)
* It helps prevent things like syntax errors, typos, bad formatting, incorrect styling, etc
* It saves our time as a developer
* If you are working in a team, it saves time for people who are reviewing your code (no need to distrust for typos and formatting issues)

For this repo I am using flake8 as a linter.

To run flake8 over all files in repo simply run:
```bash
flake8
```
in the terminal. To run it for a specific file
```bash
flake8 model/add_numbers.py
```
Flake8 can also be added to your editor.

You can find more information at [What is Flake8, and why should we use it?](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2).

## Other useful tools:
* [Black](https://black.readthedocs.io/en/stable/index.html): Python code formatter
* [Isort](https://pycqa.github.io/isort/): Python library to sort imports alphabetically, and automatically separated into sections and by type.

# Github Actions
GitHub Actions is a continuous integration and continuous delivery platform that allows you to automate your 
build, test, and deployment pipeline. You can create workflows that build and test every pull request to your 
repository, or deploy merged pull requests to production.

You can find more information at (Github Actions documentation)[https://docs.github.com/en/actions].