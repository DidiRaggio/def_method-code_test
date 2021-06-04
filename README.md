# text_processor

## Text Processor Package

The Text Processor repository contains an `text_processor` Python package which can be installed in the usual ways (i.e. using `pip install` or `python setup.py`).

### Dependencies

The the setup.py requires a Python version greater than 3.7 as well as Pytest and Pytest-Mock.

### Package Installation

The recommended installation procedure for development is to create a separate, dedicated Conda environment for the project and to install the package using `pip`.

Create a `conda` environment:

```bash
conda create --name def_method python=3.7
```

Activate the `conda` environment:

```bash
conda activate def_method
```

Install the `text_processor` package in the `conda` environment:

```bash
pip install .
```



### Execution

Run the `text_processor` from any directory, passing in the path to the file to be processed:

```bash
text_processor <file_path>
```



### Testing

Tests where written using the Pytest and Pytest-Mock distributions.

From a terminal in the project folder run:

```bash
pytest -s -vv
```

