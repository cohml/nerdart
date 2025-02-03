#!/usr/bin/env bash

set -e

if [[ $(command -v mamba) ]]; then
  CMD=mamba
elif [[ $(command -v conda) ]]; then
  CMD=conda
else
  echo "ERROR: ``conda`` not in PATH. Cannot create environment. Aborting."
  exit 1
fi

CONDA_ENVS_DIR="$("${CMD}" env list | grep -E "^base\s" | rev | awk '{print $1}' | rev)/envs"

usage() {
    cat <<EOF
Usage:

    ./mkenv.sh [ARGS]

Required arguments -- One and only one of the following:

    --name | -n
      Name of the environment. Will be installed into
      ``${CONDA_ENVS_DIR}/<name>`` unless
      otherwise specified in ``.condarc``.

    --prefix | -p
      Prefix (directory) for the environment. Will be
      installed into the specified directory.

Optional arguments:

  --help | -h
      Print out usage details.

EOF
}

if [[ "$#" -eq 0 ]]; then
  printf "ERROR: Too few arguments passed.\n\n"
  usage
  exit 1
fi

while [[ -n "${1}" ]]; do
  case "${1}" in
    --help|-h)
      usage
      exit 0
      ;;
    --name|-n)
      shift
      NAME="${1}"
      ;;
    --prefix|-p)
      shift
      PREFIX="${1}"
      ;;
    *)
      printf "ERROR: Unrecognized argument: \"%s\". Exiting.\n\n" "${1}"
      usage
      exit 1
      ;;
  esac
  shift
done

if [[ -z "${NAME}" ]]; then
  ARGS=( --prefix "${PREFIX}" )
else
  ARGS=( --name "${NAME}" )
fi

"${CMD}" env create --file environment.yaml "${ARGS[@]}"
