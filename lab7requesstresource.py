import simpy


def service(env, counter):
    with counter.request() as request:
        yield request

        print('Service starts at', env.now)
        yield env.timeout(4)
        print('Service ends at', env.now)


def customer(env, name, counter, service_time):
    arrival_time = env.now
    print(name, 'arrives at', arrival_time)

    with counter.request() as request:
        yield request

        wait = env.now - arrival_time
        print(name, 'waited', wait)

        yield env.timeout(service_time)
        print(name, 'leaves at', env.now)


def customer_generator(env, counter):
    for i in range(5):
        env.process(customer(env, f'Customer {i + 1}', counter, 4))
        yield env.timeout(2)


env = simpy.Environment()
counter = simpy.Resource(env, capacity=1)

env.process(customer_generator(env, counter))

env.run()
