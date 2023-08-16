#!/bin/bash

if [[ "$@" =~ ^bash$ ]]; then
  bash
else
  conda run -p "${NERDART_ENV_DIR}" nerdart "$@"
fi
