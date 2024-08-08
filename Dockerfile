# Use the base image with macOS setup
FROM batonogov/pyinstaller-osx:latest

# Install Tcl/Tk dependencies
RUN brew install tcl-tk

# Set environment variables for Tcl/Tk
ENV TCL_LIBRARY=/usr/local/Cellar/tcl-tk/8.6.12/lib/tcl8.6
ENV TK_LIBRARY=/usr/local/Cellar/tcl-tk/8.6.12/lib/tk8.6

# Install Python dependencies
RUN pip install --upgrade pyinstaller

# Set the working directory
WORKDIR /src

# Default command
ENTRYPOINT ["pyinstaller"]
