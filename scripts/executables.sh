python -m pip install --upgrade pip

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksWin.spec \
  batonogov/pyinstaller-windows:latest

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksLinux.spec \
  batonogov/pyinstaller-linux:latest

docker run -it \
  --device /dev/kvm \
  -p 50922:10022 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e "DISPLAY=${DISPLAY:-:0.0}" \
  -e "OSX_COMMANDS=/bin/bash -c \" \
    /bin/bash -c \\\" \
    /bin/bash -c ' \
    # Install Homebrew and dependencies \
    /bin/bash -c \\'curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | /bin/bash\\' && \
    brew install python@3.10.12 && \
    pip3 install pyinstaller && \
    brew install python-tk && \
    pyinstaller --specpath PokiBooksMacOs.spec \
    ' \
    \"\"" \
  sickcodes/docker-osx:auto