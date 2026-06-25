import simpy

def student(env, name, study_time):
    print(name, 'starts studying at', env.now)
    yield env.timeout(study_time)
    print(name, 'finishes studying at', env.now)

env = simpy.Environment()
env.process(student(env, 'Ali', 3))
env.process(student(env, 'Sara', 5))
env.process(student(env, 'Ashwin', 1))
env.run()