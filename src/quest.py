class Quest:
    def __init__(self, name, description, objectives, reward):
        self.name = name
        self.description = description
        self.objectives = objectives  # List of dicts: {'description': str, 'completed': bool}
        self.reward = reward
        self.status = "not started"

    def start(self):
        self.status = "in progress"

    def check_completion(self):
        if all(obj['completed'] for obj in self.objectives):
            self.status = "completed"
            return True
        return False

    def complete(self):
        self.status = "completed"
        return self.reward

# Example quest: Give the librarian the Necronomicon from the workshed
give_librarian_necronomicon = Quest(
    name="Deliver the Necronomicon",
    description="Retrieve the Necronomicon from the workshed and give it to the librarian.",
    objectives=[
        {"description": "Find the Necronomicon in the workshed.", "completed": False},
        {"description": "Give the Necronomicon to the librarian.", "completed": False}
    ],
    reward={"xp": 100, "item": "Librarian's Gratitude"}
)

# Example functions to update quest progress
def player_finds_necronomicon(quest):
    quest.objectives[0]['completed'] = True
    quest.check_completion()

def player_gives_book_to_librarian(quest, inventory):
    if "Necronomicon" in inventory and quest.objectives[0]['completed']:
        quest.objectives[1]['completed'] = True
        if quest.check_completion():
            reward = quest.complete()
            print("Quest complete! Reward:", reward)
    else:
        print("You don't have the Necronomicon or haven't found it yet.")

# Example usage:
# inventory = []
# give_librarian_necronomicon.start()
# player_finds_necronomicon(give_librarian_necronomicon)
# inventory.append("Necronomicon")
# player_gives_book_to_librarian(give_librarian_necronomicon, inventory)