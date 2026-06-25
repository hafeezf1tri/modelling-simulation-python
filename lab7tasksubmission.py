import simpy

def student(env):
    print('Before study timeout at', env.now)
    yield env.timeout(5)
    print('After study timeout at', env.now)

    print('Before rest timeout at', env.now)
    yield env.timeout(1)
    print('After rest timeout at', env.now)

env = simpy.Environment()
env.process(student(env))
env.run()
