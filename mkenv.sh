#!/usr/bin/env bash

set -e

usage() {
    cat <<EOF
Usage:

    sh mkenv.sh [ARGS]

Required arguments -- One and only one of the following:

    --name | -n
      Name of the environment. Will be installed into
      \`\`<conda_installation_dir>/envs/<name>\`\` unless
      otherwise specified in \`\`.condarc\`\`.

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

while [[ "$1" != "" ]]; do
  case "$1" in
    --help|-h)
      usage
      exit 0
      ;;
    --name|-n)
      shift
      NAME="$1"
      ;;
    --prefix|-p)
      shift
      PREFIX="$1"
      ;;
    *)
      printf "ERROR: Unrecognized argument: \"${1}\". Exiting.\n\n"
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

CMD=$(command -v mamba > /dev/null && echo mamba || echo conda)
"${CMD}" env create --file environment.yaml "${ARGS[@]}"
