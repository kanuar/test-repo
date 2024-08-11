URL := https://github.com/mortbopet/Ripes/releases/download/v2.2.5/Ripes-v2.2.5-linux-x86_64.AppImage
all: dependencies test

dependencies:
  sudo apt-get update
  curl -L $(URL) --output ripes.AppImage
  chmod a+x ripes.AppImage
test:
  bash run.sh
