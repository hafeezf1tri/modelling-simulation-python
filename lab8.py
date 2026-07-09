import random
import simpy


def patient(env, name, doctor):
    arrival_time = env.now
    print(f"{name} arrived at time {arrival_time}")

    with doctor.request() as request:
        yield request

        service_start = env.now
        waiting_time = service_start - arrival_time

        print(f"{name} started consultation at time {service_start}")
        print(f"{name} waited for {waiting_time} minutes")

        consultation_time = random.randint(4, 8)
        yield env.timeout(consultation_time)
        print(f"{name} finished consultation at time {env.now}")
        print(f"{name} left clinic at time {env.now}")


def patient_generator(env, doctor):
    for i in range(5):
        env.process(patient(env, f"Patient {i + 1}", doctor))
        arrival_gap = random.randint(1, 4)
        yield env.timeout(arrival_gap)


env = simpy.Environment()
doctor = simpy.Resource(env, capacity=2)

env.process(patient_generator(env, doctor))
env.run()
