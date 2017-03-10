import random

def get_coffee_machine_status():
    if random.random() < 0.5:
        return "Brewing"
    else:
        return "Waiting"

