import ray
from ray import tune

ray.shutdown()

ray.init()

tune.run("PPO",
         config={"env":"HalfCheetah-v4"}
    )


