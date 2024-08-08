#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <new_version>"
    exit 1
fi

new_version=$1

# Update version in PokiBooksMacOs.spec
sed -i "" "s/Version: [0-9]*\.[0-9]*\.[0-9]*/Version: $new_version/" PokiBooksMacOs.spec

# Update version in pyproject.toml
sed -i "" "s/version = '[0-9]*\.[0-9]*\.[0-9]*'/version = '$new_version'/" pyproject.toml

echo "Version updated to $new_version in both files."
