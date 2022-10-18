#!/usr/bin/env bash
set -e
conda env create --file environment.yaml
conda activate nerdart
pip install --editable .
conda deactivate
