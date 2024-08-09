#!/bin/bash

# Update and install Homebrew
echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Ensure Homebrew is available in the PATH
export PATH="/opt/homebrew/bin:$PATH"
echo "Homebrew installed and PATH set."

# Install Python 3.10.12
echo "Installing Python 3.10.12..."
brew install python@3.10.12

# # Install Python Tkinter
# echo "Installing Python Tkinter..."
# brew install python-tk

# Upgrade pip and install PyInstaller
echo "Upgrading pip and installing PyInstaller..."
pip3 install --upgrade pip
pip3 install pyinstaller

# Run PyInstaller with the specified spec file
echo "Running PyInstaller with PokiBooksMacOs.spec..."
pyinstaller --specpath PokiBooksMacOs.spec

echo "Build process complete."
