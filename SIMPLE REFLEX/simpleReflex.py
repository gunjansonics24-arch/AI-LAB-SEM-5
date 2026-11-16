
def simple_reflex_agent(location, status):

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"


def vacuum_world():

    environment = {
        "A": "Dirty",
        "B": "Dirty"
    }

    location = "A"

    print("Initial Environment:", environment)

    while "Dirty" in environment.values():

        status = environment[location]

        print("\nCurrent Location:", location)
        print("Current Status:", status)

        action = simple_reflex_agent(location, status)

        print("Action:", action)

        if action == "Suck":
            environment[location] = "Clean"

        elif action == "Move Right":
            location = "B"

        elif action == "Move Left":
            location = "A"

        print("Environment:", environment)

    print("\nAll rooms are clean!")
    print("Goal Achieved!")


vacuum_world()
