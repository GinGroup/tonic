#!/bin/bash
#
# Run tests on Travis CI worker.

#Exit on error
set -e
#enable logging
set -x

if [ -z "$TEST_ENV" ]; then
#No test environment is set, we run all the tests, build the docs and do black
    pytest --cov=tonic/ tonic test
    sphinx-build -b html doc/source/ doc/build/
    black --check tonic/
elif [ "$TEST_ENV" = "py36-test" ]; then
    pytest --cov=tonic/ tonic test
elif [ "$TEST_ENV" = "doc" ]; then
    sphinx-build -b html doc/source/ doc/build/
elif [ "$TEST_ENV" = "black" ]; then
     black --check tonic/
else
    echo Uknown test environment
fi
echo Passed tests
