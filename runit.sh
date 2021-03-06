#!/bin/bash

# Parse the command line
MODE="run"
if [ "$1" == "test" ]; then
  MODE="test"
  shift
fi

NAME=$1
shift

if [ -z "$NAME" ]; then
  echo "usage: $0 [test] problem [args]"
  exit 0
fi

# Look for the problem
PDIR=`find rosalind -name $NAME -type d -print`

if [ -z "$PDIR" ]; then
  echo "Could not locate problem $NAME."
  exit 0
fi

PNAME=`echo $PDIR | tr '/' '.'`

# Figure out the name of the module
if [ $MODE == "test" ]; then
  MODULE="$PNAME.test_main"
  ARGS=""
else
  MODULE="$PNAME.main"
  ARGS="$*"
  if [ -z "$ARGS" ]; then
    ARGS="sample1.txt"
  fi
fi

# Run it
# echo "Executing python module: $MODULE"
# NOTES: -B prevents creation of .pyc files
python -m $MODULE $ARGS

