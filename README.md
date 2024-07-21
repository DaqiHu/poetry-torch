# poetry-torch

A template for PyTorch users to install the correct version for your device.

## Usage

Make sure Poetry is installed on your device.

Use this to install all dependencies (including `torch`):

```shell
poetry run install
```

This will call the `install_torch.py` script and `poetry install` command in sequence.

Note that you can write your dependencies in `pyproject.toml` or in `install_torch.py` by command line.

`torch` versions are not locked by Poetry by default, please use with caution.

## Diagnostic

You may receive a warning like this:

```
Warning: 'install' is an entry point defined in pyproject.toml, but it's not installed as a script. You may get improper `sys.argv[0]`.

The support to run uninstalled scripts will be removed in a future release.

Run `poetry install` to resolve and get rid of this message.
```

That's because at this point the `.venv` is not created, and Poetry is using global `python.exe` to interpret this script. 

This will not affect package installation. They will be installed in venv as usual. Please just ignore this warning message.
