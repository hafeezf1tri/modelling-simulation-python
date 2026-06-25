import simpy

def student(env):
    print('Start studying at', env.now)
    yield env.timeout(5)
    print('Take a break at', env.now)

env = simpy.Environment()
env.process(student(env))
env.run()
