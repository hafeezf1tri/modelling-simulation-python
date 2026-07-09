import random
import simpy


def patient(env, name, counter, priority, patient_type, normal_waits, urgent_waits):
    arrival = env.now
    print(f"{name} ({patient_type}) arrived at time {arrival}")

    with counter.request(priority=priority) as req:
        yield req

        service_start = env.now
        wait = env.now - arrival

        if patient_type == "urgent":
            urgent_waits.append(wait)
        else:
            normal_waits.append(wait)

        print(f"{name} ({patient_type}) started consultation at time {service_start}")
        print(f"{name} waited for {wait} minutes")

        service = random.randint(3, 7)
        yield env.timeout(service)
        print(f"{name} finished consultation at time {env.now}")
        print(f"{name} left clinic at time {env.now}")


def patient_generator(env, counter, normal_waits, urgent_waits):
    for i in range(1, 21):
        if i % 5 == 0:
            priority = 1
            patient_type = "urgent"
        else:
            priority = 2
            patient_type = "normal"

        env.process(
            patient(
                env,
                f"Patient {i}",
                counter,
                priority,
                patient_type,
                normal_waits,
                urgent_waits,
            )
        )
        arrival_gap = random.randint(1, 4)
        yield env.timeout(arrival_gap)


def run_simulation(num_counters):
    env = simpy.Environment()
    counter = simpy.PriorityResource(env, capacity=num_counters)
    normal_waits = []
    urgent_waits = []

    env.process(patient_generator(env, counter, normal_waits, urgent_waits))
    env.run()

    normal_avg = sum(normal_waits) / len(normal_waits)
    urgent_avg = sum(urgent_waits) / len(urgent_waits)

    return normal_avg, urgent_avg


normal_avg, urgent_avg = run_simulation(1)

print(f"Average normal patient wait: {normal_avg}")
print(f"Average urgent patient wait: {urgent_avg}")
