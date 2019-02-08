import os
import random
import shelve
from enum import Enum

import arcade

import src.word
import src.star

class GameStates(Enum):
    GAME_OVER = 0
    RUNNING = 1

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Space Typer")
        arcade.set_background_color((5, 2, 27))

        self.screen_width = width
        self.screen_height = height

        self.high_score = int()

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
            self.screen_width / 2, (self.screen_height / 2) + 68,
            arcade.color.WHITE, 54,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text("Press SPACE to restart",
            self.screen_width / 2, (self.screen_height / 2),
            arcade.color.WHITE, 24,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text(f"Current score : {self.score}", 15, 15,arcade.color.WHITE, 14,)
        arcade.draw_text(f"High score : {self.high_score}", self.screen_width - 15, 15, arcade.color.WHITE, 14,
            align="right", anchor_x="right", anchor_y="baseline"
        )
    
    def draw_game(self):
        for word in self.word_list:
            word.draw()
        
        arcade.draw_text(f"Score : {self.score}", 15, 15, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives : {self.lives}", self.screen_width - 15, 15, arcade.color.WHITE, 14, align="right", anchor_x="right", anchor_y="baseline")

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
            row = random.randrange(src.word.WORD_ROW_COUNT)
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
            rand_word = random.choice(src.word.WORD_LIST)
            if rand_word[0] not in occupied_chars:
                break
        
        self.word_list.add(src.word.Word(rand_word, row, self.screen_width, self.screen_height))

    def create_star(self):
        self.star_list.add(src.star.Star(self.screen_width, self.screen_height))
    
    def update(self, delta_time):
        """ Movement and game logic """
        for star in self.star_list:
            star.x -= star.speed * delta_time
            if star.x < 0:
                star.reset_pos(self.screen_width, self.screen_height)

        if self.state == GameStates.RUNNING:
            for word in self.word_list:
                word.x -= 100 * delta_time
                if word.x < 0:
                    if self.focus_word == word:
                        self.focus_word = None

                    self.lives -= 1

                    self.word_list.discard(word)
                    self.create_word()
            
            if self.lives <= 0:
                path = os.path.join(os.path.expanduser("~"), ".space-typer")
                score_file = shelve.open(path)
                new_high_score = int()
                if score_file.get("high_score") == None:
                    new_high_score = self.score
                else:
                    new_high_score = max([self.score, score_file["high_score"]])
                score_file["high_score"] = new_high_score
                self.high_score = new_high_score

                self.state = GameStates.GAME_OVER
    
    def on_key_press(self, key, modifiers):
        if key > 127:
            return

        if self.state == GameStates.GAME_OVER and key == 32:
            self.setup()
            self.state = GameStates.RUNNING

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