python -m pip install --upgrade pip

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksWin.spec \
  batonogov/pyinstaller-windows:latest

docker run \
  --volume "$(pwd):/src/" \
  --env SPECFILE=./PokiBooksLinux.spec \
  batonogov/pyinstaller-linux:latest

