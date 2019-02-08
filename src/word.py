import arcade

WORD_ROW_COUNT = 20
WORD_LIST = ("pull", "limping", "thaw", "placid", "record", "untidy", "tested",
        "heartbreaking", "hurt", "assorted", "servant", "stale", "talk",
        "snake", "desk", "advertisement", "balance", "cut", "animated",
        "loaf", "reading", "massive", "rhetorical", "reminiscent", "pig",
        "ray", "wrestle", "upbeat", "person", "addition", "record", "left",
        "lively", "rain", "tick", "knot", "remarkable", "neat", "yam", "sea",
        "amuse", "whirl", "thoughtful", "painstaking", "dysfunctional",
        "female", "threatening", "marked", "linen", "rinse", "word",
        "perfect", "hallowed", "dangerous", "birth", "pumped", "available",
        "coherent", "macabre", "early", "loss", "dam", "true", "berry",
        "unaccountable", "drop", "righteous", "nest", "attack", "smoggy",
        "lettuce", "crib", "mighty", "ratty", "short", "tall", "thankful",
        "aunt", "haunt", "wild", "pull", "brave", "property", "vague", "stove",
        "glass", "black-and-white", "floor", "cart", "blushing", "yellow",
        "daffy", "can", "gruesome", "screw", "wonder", "minor", "rotten",
        "exultant", "fearless", "box", "action", "probable", "verdant",
        "warlike", "wrathful", "support", "cooing", "piquant", "instrument",
        "development", "fire", "late", "rainstorm", "sad", "trust", "perform",
        "press", "spotless", "lyrical", "yell", "finger", "purring", "load",
        "vivacious", "parsimonious", "quack", "bury", "hellish", "selective",
        "leather", "quilt", "deserve", "obsolete", "repeat", "prose", "real",
        "chief", "delicious", "saw", "fold", "move", "pump", "size", "tart",
        "cover", "pets", "wheel", "mate", "rate", "coach", "honorable", "shake",
        "picture", "sprout", "mother", "toes", "interfere", "skinny", "alarm",
        "authority", "questionable", "cub", "enthusiastic", "wistful", "organic",
        "step", "behavior", "zonked", "dry", "alcoholic", "average", "stomach",
        "trade", "street", "panicky", "creepy", "relieved", "use", "animal",
        "distance", "soggy", "part", "worthless", "ball", "precious", "quiet",
        "arithmetic", "excited", "festive", "unequaled", "sincere", "hissing",
        "bruise", "pin", "key", "modern", "pigs", "foregoing", "attempt", "continue",
        "horse", "beautiful", "miscreant", "boorish", "book", "dress", "grey",
        "children", "bustling", "super", "secret", "message", "lock", "giants",
        "squash", "funny", "kindhearted", "classy", "mountain", "boil", "far",
        "hand", "curly", "hysterical", "thirsty", "attraction", "neighborly",
        "experience", "mellow", "knife", "woebegone", "rambunctious", "provide",
        "fragile", "obedient", "power", "jagged", "scrawny", "flag", "government",
        "unruly", "skip", "mess", "incandescent", "bucket", "bird", "desire",
        "nod", "shiny", "spotty", "care", "basin", "coat", "cave", "robin",
        "slippery", "mushy", "hand", "stormy", "fill", "phone", "scale", "unequal",
        "tightfisted", "attend", "nice", "lavish", "cough", "black", "request",
        "embarrassed", "absent", "kick", "tomatoes", "imaginary", "blue-eyed", "shirt",
        "blood", "misty", "shelf", "sulky", "onerous", "resolute", "salty", "sweater",
        "owe", "boring", "adjoining", "lacking", "separate", "shoes", "thread",
        "highfalutin", "ritzy", "apparel", "matter", "existence", "educated", "shocking",
        "rough", "food", "prefer")

class Word:
    def __init__(self, word, row, screen_width, screen_height):
        self.word = word
        self.row = row
        self.x = screen_width
        self.y = (int((screen_height - 50) / WORD_ROW_COUNT) * row) + 50
        self.in_focus = False
    
    def draw(self):
        arcade.draw_text(self.word, self.x, self.y,
            arcade.color.DODGER_BLUE if self.in_focus else arcade.color.WHITE,
        14)
    
    def attack(self):
        self.word = self.word[1:]