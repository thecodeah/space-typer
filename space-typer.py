import arcade
import random
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WORD_ROW_COUNT = 20

words = ("pull", "limping", "thaw", "placid", "record", "untidy", "tested",
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
        "children", "bustling", "lock", "giants", "squash", "funny", "kindhearted",
        "classy", "mountain", "boil", "far", "hand", "curly", "hysterical",
        "thirsty", "attraction", "neighborly", "experience", "mellow", "knife",
        "woebegone", "rambunctious", "provide", "fragile", "obedient", "power",
        "jagged", "scrawny", "flag", "government", "unruly", "skip", "mess",
        "incandescent", "bucket", "bird", "desire", "nod", "shiny", "spotty",
        "care", "basin", "coat", "cave", "robin", "slippery", "mushy", "hand",
        "stormy", "fill", "phone", "scale", "unequal", "tightfisted", "attend",
        "nice", "lavish", "cough", "black", "request", "embarrassed", "absent",
        "kick", "tomatoes", "imaginary", "blue-eyed", "shirt", "blood", "misty",
        "shelf", "sulky", "onerous", "resolute", "salty", "sweater", "owe", "boring",
        "adjoining", "lacking", "separate", "shoes", "thread", "highfalutin",
        "ritzy", "apparel", "matter", "existence", "educated", "shocking", "rough",
        "food", "prefer")

class GameStates(Enum):
    GAME_OVER = 0
    RUNNING = 1

class Star:
    def __init__(self):
        self.x = random.randrange(SCREEN_WIDTH + 200)
        self.y = random.randrange(SCREEN_HEIGHT)
        self.size = random.randrange(4)
        self.speed = random.randrange(20, 40)
        self.color = random.choice([arcade.color.PURPLE, arcade.color.BLUEBERRY])
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
    
    def reset_pos(self):
        self.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.y = random.randrange(SCREEN_HEIGHT)

class Word:
    def __init__(self, word, row):
        self.word = word
        self.row = row
        self.x = SCREEN_WIDTH
        self.y = (int((SCREEN_HEIGHT - 50) / WORD_ROW_COUNT) * row) + 50
        self.in_focus = False
    
    def draw(self):
        arcade.draw_text(self.word, self.x, self.y,
            arcade.color.DODGER_BLUE if self.in_focus else arcade.color.WHITE,
        14)
    
    def attack(self):
        self.word = self.word[1:]

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Space Typer")
        arcade.set_background_color((5, 2, 27))

        self.score = int()
        self.lives = int()
        self.state = None
        self.focus_word = None # The word that is currently being focused on / typed

        self.word_list = set()
        self.star_list = set()

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.score = 0
        self.lives = 3
        self.state = GameStates.RUNNING
        self.focus_word = None
        
        self.star_list = set()
        self.word_list = set()

        for _ in range(5):
            self.create_word()
        for _ in range(25):
            self.create_star()
            
    
    def draw_game_over(self):
        arcade.draw_text("Game Over",
            SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 54,
            arcade.color.WHITE, 54,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text("Click to restart",
            SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 24,
            arcade.color.WHITE, 24,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text(f"Score : {self.score}", 10, SCREEN_HEIGHT - 10, arcade.color.WHITE, 15, anchor_x="left", anchor_y="top")
    
    def draw_game(self):
        for word in self.word_list:
            word.draw()
        
        arcade.draw_text(f"Score : {self.score}", 15, 15, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives : {self.lives}", SCREEN_WIDTH - 15, 15, arcade.color.WHITE, 14, align="right", anchor_x="right", anchor_y="baseline")

    def on_draw(self):
        arcade.start_render()

        for star in self.star_list:
            star.draw()

        if self.state == GameStates.RUNNING:
            self.draw_game()
        else:
            self.draw_game_over()
    
    def create_word(self):
        # Find a row that's currently not occupied by another word.
        row = int()
        occupied_rows = set()
        while True:
            row = random.randrange(WORD_ROW_COUNT)
            for word in self.word_list:
                occupied_rows.add(word.row)
            if row not in occupied_rows:
                break
        
        # Find a word that starts with a character that is not the first
        # character of another word.
        occupied_chars = set()
        for word in self.word_list:
            occupied_chars.add(word.word[0])
        rand_word = str()
        while True:
            rand_word = random.choice(words)
            if rand_word[0] not in occupied_chars:
                break
        
        self.word_list.add(Word(rand_word, row))

    def create_star(self):
        self.star_list.add(Star())
    
    def update(self, delta_time):
        """ Movement and game logic """
        for star in self.star_list:
            star.x -= star.speed * delta_time
            if star.x < 0:
                star.reset_pos()

        if self.state == GameStates.RUNNING:
            for word in self.word_list:
                word.x -= 100 * delta_time
                if word.x < 20:
                    if self.focus_word == word:
                        self.focus_word = None

                    self.lives -= 1

                    self.word_list.discard(word)
                    self.create_word()
            
            if self.lives <= 0:
                self.state = GameStates.GAME_OVER
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == GameStates.GAME_OVER:
            self.setup()
            self.state = GameStates.RUNNING
    
    def on_key_press(self, key, modifiers):
        if key > 127:
            return

        if self.focus_word == None:
            for word in self.word_list:
                if word.word[0] == chr(key):
                    self.focus_word = word

                    word.attack()
                    word.in_focus = True
                    break
        else:
            if self.focus_word.word[0] == chr(key):
                    self.focus_word.attack()
                    if self.focus_word.word == "":
                        self.word_list.discard(self.focus_word)
                        self.focus_word = None
                        self.score += 1
                        self.create_word()

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()