# Unitree RL environments migration to Isaac Lab

## Overview

This folder migrates Unitree RL environments to [Isaac Lab](https://github.com/isaac-sim/IsaacLab), which is verified with the latest release.

## Installation

- Install Isaac Sim and Isaac Lab 
    - We recommend using the conda installation as it simplifies calling Python scripts from the terminal.
        ```bash
        conda create -n env_isaaclab python=3.10
        conda activate env_isaaclab
        # notice the CUDA version available on your system
        pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121 
        pip install --upgrade pip
        pip install isaaclab[isaacsim,all]==2.1.0 --extra-index-url https://pypi.nvidia.com
        ```
    - The installation process takes about 10 minutes. Once done, please validate the installation by:
        ```bash
        # note: you can pass the argument "--help" to see all arguments possible.
        isaacsim
        ```

    - by following the [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html), you can also refer to the binary installation and docker deployment.

- Install the Unitree RL IsaacLab standalone environments.
    - Clone or copy this project/repository separately from the Isaac Lab installation (i.e. outside the `IsaacLab` directory):

    - Use a python interpreter that has Isaac Lab installed, install the library in editable mode using:
        ```bash
        conda activate env_isaaclab
        cd unitree_rl_gym/unitree_rl_lab
        python -m pip install -e source/unitree_rl_lab
        ```

- Verify that the environments are correctly installed by:

    - Listing the available tasks:

        ```bash
        python scripts/list_envs.py
        ```

    - Running a task:

        ```bash
        python scripts/rsl_rl/train.py --task unitree_g1 --num_envs 4096 --headless --max_iterations <10000>
        ```

    - Inference with a trained agent:

        ```bash
        python scripts/rsl_rl/play.py --task unitree_g1 --num_envs 32
        ```

    - Running a task with dummy agents:

        These include dummy agents that output zero or random agents. They are useful to ensure that the environments are configured correctly.

        - Zero-action agent

            ```bash
            python scripts/zero_agent.py --task=unitree_g1
            ```
        - Random-action agent

            ```bash
            python scripts/random_agent.py --task=unitree_g1
            ```
