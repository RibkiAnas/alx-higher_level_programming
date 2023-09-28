#!/bin/bash
# This script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -L -f -X POST -H "Content-Type: application/json" -d @"$2" "$1"
