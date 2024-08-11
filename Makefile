all: dependencies
dependencies:
    sudo apt-get update
	sudo sysctl kernel.perf_event_paranoid=-1
    bash run.sh
