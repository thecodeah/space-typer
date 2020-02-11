import arcade
import argparse
import os
import yaml

from src.game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WORD_LIST_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words-en.yaml")


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
    parser.add_argument("--word-list", type=str, default=WORD_LIST_FILE, help="yaml file containing the words to use in the game")

    args = parser.parse_args()

    words = parse_word_list(args.word_list)

    main(args.screen_width, args.screen_height, words)
