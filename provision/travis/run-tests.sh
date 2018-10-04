#!/bin/bash
#
# Run tests on Travis CI worker.

#Exit on error
set -e
#enable logging
set -x

pytestCommand="pytest --cov=tonic/ tonic test"
blackCommand="black --check tonic/ test/"
sphinxCommand="sphinx-build -b html doc/source/ doc/build/"


if [ -z "$TEST_ENV" ]; then
#No test environment is set, we run all the tests, build the docs and do black 
    eval $pytestCommand
    eval $sphinxCommand
    eval $blackCommand
elif [ "$TEST_ENV" = "py36-test" ]; then
    eval $pytestCommand
elif [ "$TEST_ENV" = "doc" ]; then
    eval $sphinxCommand
elif [ "$TEST_ENV" = "black" ]; then
    eval $blackCommand
else
    echo "Unknown test environment"
    exit 1
fi
echo "Passed tests"
