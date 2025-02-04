#!/bin/bash

set -u

if [[ "$@" =~ ^bash$ ]]; then
  bash
else
  conda run -p "${NERDART_ENV_DIR}" nerdart "$@"
  if [[ "$@" != *"logo" && "$@" != *"ls" && "$@" != *"--help" && "$@" != *"-h" ]]; then
    "${NERDART_ENV_DIR}/bin/uvicorn" "main:app" --app-dir ${NERDART_PARENT_DIR}/app --host 0.0.0.0 --port 80
  fi
fi
