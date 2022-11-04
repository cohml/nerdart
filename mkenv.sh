#!/usr/bin/env bash

set -e

# install conda environment
conda env create --file environment.yaml

# install `nerdart` package into environment
source activate nerdart
pip install --editable .
conda deactivate
