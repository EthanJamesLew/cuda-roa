.PHONY: clean run all

ARCH ?= sm_86
NVCC = nvcc
NVCC_FLAGS = -O3 -arch=$(ARCH)
SRC_DIR = src
SCRIPTS_DIR = scripts

all: pendulum

pendulum:
	$(NVCC) $(NVCC_FLAGS) -o pendulum $(SRC_DIR)/pendulum.cu

run: pendulum
	./pendulum
	python $(SCRIPTS_DIR)/roa.py

clean:
	rm -f pendulum
	rm -f initial_states.bin
	rm -f final_states.bin
