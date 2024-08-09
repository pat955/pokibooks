#!/bin/bash

# Output file for checksums
CHECKSUM_FILE="checksums.txt"

# Create or clear the checksum file
: > "$CHECKSUM_FILE"

# Find all zip and tar.gz files in the root directory
find . -maxdepth 1 -type f \( -name "*.zip" -o -name "*.tar.gz" \) | while read -r file; do
    # Calculate checksum for each file
    checksum=$(sha256sum "$file" | awk '{print $1}')
    # Get the relative path of the file for the output
    relative_path=$(basename "$file")
    # Write the checksum and filename to the output file
    echo "$checksum  $relative_path" >> "$CHECKSUM_FILE"
done

echo "Checksums have been written to $CHECKSUM_FILE."
