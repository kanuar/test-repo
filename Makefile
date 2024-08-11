all: dependencies test
dependencies:
    sudo apt-get update
    curl -L https://github.com/mortbopet/Ripes/releases/download/v2.2.5/Ripes-v2.2.5-linux-x86_64.AppImage --output ripes.AppImage
    chmod a+x ripes.AppImage
test:
    bash run.sh
