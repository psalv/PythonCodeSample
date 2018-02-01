#!/usr/bin/env bash

curl -X POST http://pythoncodingsample.herokuapp.com/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'