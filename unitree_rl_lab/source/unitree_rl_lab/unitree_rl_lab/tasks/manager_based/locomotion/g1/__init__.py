# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##

gym.register(
    id="unitree_g1",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        #"env_cfg_entry_point": "isaaclab_tasks.manager_based.locomotion.velocity.config.g1.rough_env_cfg:G1RoughEnvCfg",
        "env_cfg_entry_point": f"{__name__}.g1_env_cfg:G1RoughCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:LeggedRobotCfgPPO",
    },
)

