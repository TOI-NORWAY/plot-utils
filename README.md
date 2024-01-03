# Python Package Template

## Inventory

- `.devcontainer`: Configuration for the VSCode development container.
- `.github/CODEOWNERS`: Defines the default reviewers for your package's pull requests.
- `examples/`: Examples of how to use your package in a script or in a notebook.
- `pyproject.toml`: Info about the package and its dependencies.
- `README.md`: This file.
- `src/plotutils`: The python package with modules (`*.py` files).

## About

- This package template follows setuptool's [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).
- To follow [PEP 621](https://peps.python.org/pep-0621/), `pyproject.toml` is used to specify the package's dependencies and metadata.
- To get a `<TOI_PACKAGE_TOKEN>`, TØI's GitHub admin has to create a [fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#fine-grained-personal-access-tokens) with *read-only* access to the repro.

## How to use

See [`examples/example.py`](examples/example.py) or [`examples/example.ipynb`](examples/example.ipynb) for an example of how to use your package in a script or in a notebook.

## How to install your package

Replace `<VERSION>` with any available version number from your package's repository and `plotutils` with the name of your package.

### Install with pip

Add the following to your `requirements.txt` file:

```txt
plotutils @ git+https://<TOI_PACKAGE_TOKEN>@github.com/TOI-NORWAY/<REPRO_NAME>.git@v<VERSION>
```

or run the following command:

```bash
pip install "plotutils @ git+https://<TOI_PACKAGE_TOKEN>@github.com/TOI-NORWAY/<REPRO_NAME>.git@v<VERSION>"
```

### Install with Poetry

Add the following to your `pyproject.toml` file's `[tool.poetry.dependencies]` section:

```txt
plotutils = { git = "https://<TOI_PACKAGE_TOKEN>@github.com/TOI-NORWAY/<REPRO_NAME>.git", tag = "v<VERSION>" }
```
