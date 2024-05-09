def probability(rho: float, num: int) -> float:
    return rho ** num * (1 - rho)

def prob_min(min_num: int, rho: float) -> float:
    prob_min = 0.0
    for i in range(min_num):
        prob_min += probability(rho=rho, num=i)
    return 1 - prob_min

def system_queue(arrival_rate: float, service_rate: float) -> None:
    rho = arrival_rate / service_rate
    length_system = rho / (1 - rho)
    length_queue = length_system - rho
    wait_time_system = length_system / arrival_rate
    wait_time_queue = length_queue / arrival_rate
    print(f"Length of the System = {length_system}\nLength of the Queue = {length_queue}\nTotal Wait Time of the System: {wait_time_system}\nTotal Wait Time of the Queue: {wait_time_queue}")

while True:
    arrival_rate = float(input("Enter arrival rate per hour: "))
    while arrival_rate <= 0:
        print("Arrival rate must be greater than 0")
        arrival_rate = float(input("Enter arrival rate per hour: "))

    service_rate = float(input("Enter service rate per hour: "))
    while service_rate <= 0:
        print("Service rate must be greater than 0")
        service_rate = float(input("Enter service rate per hour: "))

    print(f"The arrival rate is {arrival_rate}")
    print(f"The service rate is {service_rate}")

    rho = arrival_rate / service_rate

    print("\nProbability Calculation:")
    num_people = int(input("Enter the number of people in the system: "))
    print(f"The probability of {num_people} people being in the system is: {probability(rho=rho, num=num_people)}")

    print("\nProbability of at least 'n' people in the system:")
    min_value = int(input("Enter the minimum number of people: "))
    print(f"The probability of at least {min_value} people in the system: {prob_min(min_num=min_value, rho=rho)}")

    print("\nSystem Metrics:")
    system_queue(arrival_rate, service_rate)

    choice = input("Do you want to run the program again? (yes/no): ")
    if choice.lower() != "yes":
        exit()