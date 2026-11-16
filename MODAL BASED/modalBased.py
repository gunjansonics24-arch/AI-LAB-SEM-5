
class ModelBasedAgent:

    def __init__(self):
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

    def update_model(self, location, status):
        self.model[location] = status

    def decide_action(self, location):

        if self.model[location] == "Dirty":
            return "Suck"

        elif self.model["A"] == "Unknown":
            return "Move Left"

        elif self.model["B"] == "Unknown":
            return "Move Right"

        elif self.model["A"] == "Dirty":
            return "Move Left"

        elif self.model["B"] == "Dirty":
            return "Move Right"

        else:
            return "NoOp"


def vacuum_world():

    environment = {
        "A": "Dirty",
        "B": "Dirty"
    }

    agent = ModelBasedAgent()

    location = "A"

    print("Initial Environment:", environment)

    while True:

        status = environment[location]

        print("\nCurrent Location:", location)
        print("Current Status:", status)

        agent.update_model(location, status)

        print("Internal Model:", agent.model)

        action = agent.decide_action(location)

        print("Action:", action)

        if action == "Suck":
            environment[location] = "Clean"

        elif action == "Move Left":
            location = "A"

        elif action == "Move Right":
            location = "B"

        elif action == "NoOp":
            print("\nAll rooms are clean!")
            print("Goal Achieved!")
            break

        print("Updated Environment:", environment)


vacuum_world()
