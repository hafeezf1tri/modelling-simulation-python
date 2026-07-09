import random
import simpy


def patient(env, name, counter, wait_times):
    arrival = env.now
    print(f"{name} arrived at time {arrival}")

    with counter.request() as req:
        yield req

        service_start = env.now
        wait = env.now - arrival
        wait_times.append(wait)

        print(f"{name} started consultation at time {service_start}")
        print(f"{name} waited for {wait} minutes")

        service = random.randint(3, 7)
        yield env.timeout(service)
        print(f"{name} finished consultation at time {env.now}")
        print(f"{name} left clinic at time {env.now}")


def patient_generator(env, counter, wait_times):
    for i in range(10):
        env.process(patient(env, f"Patient {i + 1}", counter, wait_times))
        arrival_gap = random.randint(1, 4)
        yield env.timeout(arrival_gap)


def run_simulation(num_counters):
    env = simpy.Environment()
    counter = simpy.Resource(env, capacity=num_counters)
    wait_times = []

    env.process(patient_generator(env, counter, wait_times))
    env.run()

    return sum(wait_times) / len(wait_times)


avg_1 = run_simulation(1)
avg_2 = run_simulation(2)

print(f"Average wait with 1 counter: {avg_1}")
print(f"Average wait with 2 counters: {avg_2}")
