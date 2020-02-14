import arcade
import argparse
import yaml

from src.game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DEFAULT_WORD_LIST = ("pull", "limping", "thaw", "placid", "record", "untidy", "tested",
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


def main(screen_width, screen_height, words):
    game = Game(screen_width, screen_height, words)
    game.setup()
    arcade.run()


def parse_word_list(word_list_filename):
    with open(word_list_filename, "r") as word_list_file:
        data = yaml.safe_load(word_list_file)
        return data["words"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start space-typer game.")
    parser.add_argument("--screen-width", type=int, default=SCREEN_WIDTH, help="Width of screen in pixels")
    parser.add_argument("--screen-height", type=int, default=SCREEN_HEIGHT, help="Height of screen in pixels")
    parser.add_argument("--word-list", type=str, default=None,
                        help="yaml file containing the words to use in the game" +
                        " (use a list of words with key 'words'); by default use built-in word list.")

    args = parser.parse_args()

    if args.word_list:
        words = parse_word_list(args.word_list)
    else:
        words = DEFAULT_WORD_LIST

    main(args.screen_width, args.screen_height, words)
