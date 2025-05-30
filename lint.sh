#!/bin/sh
echo "Running flake8 lint check..."
flake8 rest_api/app
echo "Lint check completed!"