from dm_control import viewer
import isi_mujoco
import pdb
from isi_mujoco.models import gait10dof18musc
# Load an environment from the Control Suite.
# gait10dof18musc humanoid
# env = suite.load(domain_name="gait10dof18musc", task_name="stand")

task_kwargs = {}
env = gait10dof18musc.SUITE['run'](**task_kwargs)
env.task.visualize_reward = False

env.physics.reset(keyframe_id=0)
# print('\n'.join(dir(env.physics.model)))
# Launch the viewer application.
viewer.launch(env)