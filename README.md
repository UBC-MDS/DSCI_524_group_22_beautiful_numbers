# Beautiful Numbers

|        |        |
|--------|--------|
| Documentation | [![Documentation](https://img.shields.io/badge/docs-gh--pages-blue)](https://ubc-mds.github.io/DSCI_524_group_22_beautiful_numbers/) |
| Package | [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) |
| CI  | [![CI](https://github.com/UBC-MDS/DSCI_524_group_22_beautiful_numbers/blob/e32a2d8855564d22a2f04a4987589a58d7312e2b/.github/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_group_22_beautiful_numbers/blob/e32a2d8855564d22a2f04a4987589a58d7312e2b/.github/workflows/deploy.yml)

## Contributors

-   Jade Chen, Michael Oyatsi, Jackson Lu, Grigory Artazyan

## Summary

Beautiful Numbers is a small Python package that provides utilities for exploring common numerical properties and representations. The goal of the project is educational: to make it easy to inspect whether numbers have certain mathematical properties or to view them in alternative bases without relying on heavy external dependencies.

## Documentation

-   **Landing Page**: https://ubc-mds.github.io/DSCI_524_group_22_beautiful_numbers/
-   **API Reference**: https://ubc-mds.github.io/DSCI_524_group_22_beautiful_numbers/reference/

## Included Functions

-   `prime_list` For a given input number, this function generates a list of prime numbers up to and including the input number. This can be used for identifying prime candidates for use in cryptography.

-   `binary` Converts a non-negative integer into its binary representation, returned as a string. Useful for understanding base-2 representations and bit-level reasoning.

-   `hexa` Converts a non-negative integer into its hexadecimal representation, returned as a string. Useful for understanding base-16 representations.

-   `fib_seq` Generates the Fibonacci sequence from 1 up to a given positive integer n. The output illustrates the recursive growth pattern of the sequence.

## Installation

### For Users

Install the package from Test PyPI:

``` bash
pip install --index-url https://test.pypi.org/simple/beautifulnumbers
```

**Package URL**: https://test.pypi.org/project/beautifulnumbers/

### For Developers

1.  **Clone the repository**:

    ``` bash
    git clone https://github.com/UBC-MDS/DSCI_524_group_22_beautiful_numbers.git
    cd DSCI_524_group_22_beautiful_numbers
    ```

2.  **Set up the development environment**:

    Create a conda environment (recommended):

    ``` bash
    conda create -n beautifulnumbers python=3.12
    conda activate beautifulnumbers
    ```

3.  **Install the package in editable mode with all development dependencies**:

    ``` bash
    pip install -e ".[dev,tests,docs,build]"
    ```

    This installs:

    -   The package itself in editable mode (`-e`)
    -   Development tools (`dev`): hatch, pre-commit
    -   Testing tools (`tests`): pytest, pytest-cov, etc.
    -   Documentation tools (`docs`): quartodoc
    -   Build tools (`build`): pip-audit, twine

## Usage

``` python
from beautifulnumbers.binary import binary
from beautifulnumbers.hexa import hexa
from beautifulnumbers.fib_seq import fib_seq
from beautifulnumbers.prime_list import prime_list

# Generate prime numbers up to 20
primes = prime_list(20)
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]

# Convert to binary
bin_str = binary(42)
print(bin_str)  # "101010"

# Convert to hexadecimal
hex_str = hexa(255)
print(hex_str)  # "FF"

# Generate Fibonacci sequence up to 10
fib = fib_seq(10)
print(fib)  # [1, 1, 2, 3, 5, 8]
```

## Development Workflow

### Running Tests

Run tests with coverage report:

``` bash
pytest --cov=beautifulnumbers --cov-report=term-missing --cov-report=xml
```

### Building Documentation

1.  **Build the API reference with quartodoc**:

    ``` bash
    quartodoc build --verbose
    ```

2.  **Render the Quarto site**:

    ``` bash
    quarto render
    ```

3.  **Preview locally**:

    ``` bash
    quarto preview
    ```

### Deploying Documentation

Documentation is **automatically deployed** to GitHub Pages via GitHub Actions when you push to the `main` branch.

**Workflow**:

1.  Push changes to `main`

2.  GitHub Actions workflow (`.github/workflows/quartodoc.yml`) runs automatically:

    -   Installs dependencies
    -   Builds documentation with quartodoc
    -   Renders the Quarto site
    -   Publishes to `gh-pages` branch

**Manual deployment** (first-time setup only):

``` bash
quarto publish gh-pages
```

View the deployed documentation [here](https://ubc-mds.github.io/DSCI_524_group_22_beautiful_numbers/).

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution to Python Ecosystem

Much of this functionality exists in the Python standard library or in established scientific packages, this package does not aim to replace those tools. Instead, it provides a minimal, self-contained set of functions with explicit logic that is easy to read and reason about.