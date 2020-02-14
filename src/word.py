import arcade

class Word:
    def __init__(self, word, row, screen_width, screen_height, word_row_count):
        self.word = word
        self.row = row
        self.x = screen_width
        self.y = (int((screen_height - 50) / word_row_count) * row) + 50
        self.in_focus = False
    
    def draw(self):
        arcade.draw_text(self.word, self.x, self.y,
            arcade.color.DODGER_BLUE if self.in_focus else arcade.color.WHITE,
        14)
    
    def attack(self):
        self.word = self.word[1:]
