python -m pip install --upgrade pip

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksWin.spec \
  batonogov/pyinstaller-windows:latest

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksLinux.spec \
  batonogov/pyinstaller-linux:latest

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksMacOs.spec \
  --entrypoint /bin/sh batonogov/pyinstaller-linux:latest \
  -c "brew install tcl-tk && /entrypoint.sh"