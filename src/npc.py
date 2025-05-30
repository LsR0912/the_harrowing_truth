from utils.print_helper import slow_print

class NPC:
    """Non-player character for The Harrowing Truth."""

    def __init__(self,id, name, description, dialogue=None, inventory=None, hostile=False):
        self.id = id
        self.name = name
        self.description = description
        self.dialogue = dialogue or []
        self.inventory = inventory or []
        self.hostile = hostile

    def talk(self):
        if self.dialogue:
            for line in self.dialogue:
                slow_print(f"{self.name} says: \"{line}\"")
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

    def get_npcs():
        return npcs

npcs = {
    "1": NPC(1,"The Whispering Librarian","a sentient bookshelf that knows your secrets",["Ah, a visitor. The shelves groan with your presence. Do you seek answers, or merely the thrill of the unknown?"],[],False),
    "2": NPC(2,"Vorath"," A gaunt, ashen figure with eyes that flicker between light and shadow. His body is a patchwork of rotting flesh and crystalline veins that pulse with dark energy.",[],[],False),
    "3": NPC(3,"Abdul Alhazred","Speaks in a rasping whisper, echoing with the voices of the dead.",["The world is a lie. You are already dead. Join me in the eternal dark."],[],False),
    "4": NPC(4,"The Whispering Librarian","a sentient bookshelf that knows your secrets",["Ah, a visitor. The shelves groan with your presence. Do you seek answers, or merely the thrill of the unknown?"],[],False),
}
