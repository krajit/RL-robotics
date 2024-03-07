import ray
from ray import tune

ray.shutdown()

ray.init()

tune.run("DQN",
         config={"env":"CartPole-v1"},
    )


