# CUDA ROA

This project implements a fast, parallel method for estimating the region of attraction for a controlled inverted pendulum using CUDA. It utilizes millions of individual pendulum simulations to identify the initial states that lead to stable behavior. Results from these simulations are used to plot the region of attraction.

## Usage

To build the pendulum simulation and run it, use the following commands:
```shell
make run
```
This will compile the CUDA code, run the simulation, and generate the region of attraction plot.

## Customization

You can customize the architecture by setting the ARCH variable in the Makefile. By default, it is set to sm_86.

