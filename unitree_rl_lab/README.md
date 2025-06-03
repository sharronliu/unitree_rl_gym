# Unitree RL environments migration to Isaac Lab

## Overview

This project/repository migrates Unitree RL environments to Isaac Lab, currently verified with v2.1.0 release.

## Installation

- Install Isaac Lab by following the [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html).
  We recommend using the conda installation as it simplifies calling Python scripts from the terminal.

- Clone or copy this project/repository separately from the Isaac Lab installation (i.e. outside the `IsaacLab` directory):

- Using a python interpreter that has Isaac Lab installed, install the library in editable mode using:

    ```bash
    conda activate <env_isaaclab>
    cd unitree_rl_gym/unitree_rl_lab
    python -m pip install -e source/unitree_rl_lab

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
