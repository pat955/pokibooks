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
  -v "$(pwd)/build_macos.sh:/build_macos.sh" \
  -v "$(pwd):/src" \
  sickcodes/docker-osx:auto /bin/bash /build_macos.sh
