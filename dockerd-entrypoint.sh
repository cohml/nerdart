#!/bin/bash

set -u

if [[ "$@" =~ ^bash$ ]]; then
  bash
else
  conda run -p "${NERDART_ENV_DIR}" nerdart "$@"
fi
