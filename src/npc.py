from utils.print_helper import slow_print

class NPC:
    """Non-player character for The Harrowing Truth."""

    def __init__(self, id, name, description, dialogue_tree=None, inventory=None, hostile=False):
        self.id = id
        self.name = name
        self.description = description
        self.dialogue_tree = dialogue_tree or {}
        self.dialogue_state = "start"
        self.inventory = inventory or []
        self.hostile = hostile

    def talk(self):
        """Return (npc_line, [answers]) for the current dialogue state."""
        if self.dialogue_state in self.dialogue_tree:
            npc_line, answers = self.dialogue_tree[self.dialogue_state]
            return f'{self.name} says: "{npc_line}"', answers
        else:
            return f"{self.name} has nothing to say.", []

    def respond(self, answer):
        """Advance the dialogue state based on the player's answer."""
        # Each answer should map to a new state in the dialogue_tree
        if self.dialogue_state in self.dialogue_tree:
            _, answers = self.dialogue_tree[self.dialogue_state]
            if answer in answers:
                # Use answer text as the next state key, or map in a dict if needed
                next_state = answer.lower().replace(" ", "_")
                if next_state in self.dialogue_tree:
                    self.dialogue_state = next_state
                else:
                    slow_print(f"{self.name} has nothing more to say.")
            else:
                slow_print("They don't understand your response.")
        else:
            slow_print(f"{self.name} has nothing to say.")

    def give_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                return item
        return None

    def describe(self):
        slow_print(f"{self.name}: {self.description}")

    @staticmethod
    def get_npcs():
        return npcs

# Example dialogue trees
librarian_dialogue = {
    "start": (
        "Ah, a visitor. The shelves groan with your presence. Do you seek answers, or merely the thrill of the unknown?",
        ["I seek answers.", "Just exploring."]
    ),
    "i_seek_answers.": (
        "Answers come at a price. Are you willing to pay?",
        ["Yes.", "No."]
    ),
    "just_exploring.": (
        "Then tread lightly. Some knowledge cannot be unseen.",
        []
    ),
    "yes.": (
        "Very well. Ask your question, but beware the answer.",
        ["How did I get here?", "Who are you?"]
    ),
    "no.": (
        "Then begone, and do not disturb the silence.",
        []
    ),
    "how_did_i_get_here?": (
        "If you don't know, how am I supposed to know?",
        []
    ),
    "who_are_you?": (
        "I am the keeper of forbidden tomes, the memory of all who have passed through these halls.",
        []
    ),
}
abdul_dialogue = {
    "start": (
        "The world is a lie. You are already dead. Join me in the eternal dark.",
        ["Never!", "Tell me more."]
    ),
    "never!": (
        "Defiance is futile. The darkness comes for all.",
        []
    ),
    "tell_me_more.": (
        "There is peace in oblivion. Surrender, and you will understand.",
        []
    ),
}

npcs = {
    "1": NPC(1, "The Whispering Librarian", "a sentient bookshelf that knows your secrets", librarian_dialogue, [], False),
    "2": NPC(2, "Vorath", "A gaunt, ashen figure with eyes that flicker between light and shadow. His body is a patchwork of rotting flesh and crystalline veins that pulse with dark energy.", {}, [], False),
    "3": NPC(3, "Abdul Alhazred", "Speaks in a rasping whisper, echoing with the voices of the dead.", abdul_dialogue, [], False),
    "4": NPC(4, "The Whispering Librarian", "a sentient bookshelf that knows your secrets", librarian_dialogue, [], False),
}