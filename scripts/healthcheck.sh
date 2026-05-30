#!/usr/bin/env bash

curl -f http://localhost:$PORT/health/ || exit 1
