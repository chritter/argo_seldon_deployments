"""
This script creates a Conda environment from a `conda.yaml`.
The `conda.yaml` file gets fetched from cloud storage.
"""
import os
import logging
import argparse
import json
import yaml
import tempfile
import shutil
from subprocess import run
from shlex import quote


log = logging.getLogger()
log.setLevel("INFO")


# This is already set on the environment_rest and environment_grpc files, but
# we'll define a default just in case.
DEFAULT_CONDA_ENV_NAME = "mlflow"


def setup_env(model_folder):
    """Sets up a Conda environment.
    This methods creates the Conda environment described by the `MLmodel` file.
    It also injects the minimum set of dependencies described in `base.yaml` on
    this environment.
    Parameters
    --------
    model_folder
        Folder where the MLmodel files are stored.
    """
    mlmodel = read_mlmodel(model_folder)

    flavours = mlmodel["flavors"]
    pyfunc_flavour = flavours["python_function"]
    env_file_name = pyfunc_flavour["env"]
    env_file_path = os.path.join(model_folder, env_file_name)
    create_env(env_file_path)


def read_mlmodel(model_folder):
    """Reads an MLmodel file.
    Parameters
    ---------
    model_folder
        Folder where the MLmodel files are stored.
    Returns
    --------
    obj
        Dictionary with MLmodel contents.
    """
    log.info(f"Reading MLmodel file")
    mlmodel_path = os.path.join(model_folder, "MLmodel")
    return _read_yaml(mlmodel_path)


def _read_yaml(file_path):
    """Reads a YAML file.
    Parameters
    ---------
    file_path
        Path to the YAML file.
    Returns
    -------
    dict
        Dictionary with YAML file contents.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def create_env(env_file_path):
    """Creates Conda environment from YAML.
    Creates a Conda environment from a YAML file describing Python version,
    dependencies, etc.
    The new environment name is read from the `CONDA_ENV_NAME` environment
    variable.
    If the variable is not defined, it falls back to `mlflow`.
    """
    env_file_name = os.path.basename(env_file_path)
    env_name = os.getenv("CONDA_ENV_NAME", DEFAULT_CONDA_ENV_NAME)
    env_name = quote(env_name)
    env_file_path = quote(env_file_path)

    log.info(f"Creating Conda environment '{env_name}' from {env_file_name}")

    cmd = f"conda env create -n {env_name} --file {env_file_path}"
    run(cmd, shell=True, check=True)

def main():
    model_folder = "model"
    setup_env(model_folder)


if __name__ == "__main__":
    main()
