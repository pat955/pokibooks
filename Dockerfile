# Use the base image with macOS setup
FROM batonogov/pyinstaller-osx:latest

RUN system_profiler -detailLevel full > packages.txt

RUN brew install python@3.10.12

RUN brew install python-tk

# Install Python dependencies
RUN pip install --upgrade pyinstaller

