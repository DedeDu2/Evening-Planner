class EveningPlanner:
    def __init__(self):
        self.schedule = {}

    def add_event(self, time, event):
        self.schedule[time] = event

    def view_schedule(self):
        print("Evening Schedule:")
        for time, event in self.schedule.items():
            print(f"{time}: {event}")

planner = EveningPlanner()
planner.add_event("6:00 PM", "Dinner")
planner.add_event("7:00 PM", "Movie Night")
planner.add_event("9:00 PM", "Reading Time")
planner.view_schedule()
