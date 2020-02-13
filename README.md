# Space Typer

Space Typer is a typing game written in Python using the [Arcade](http://arcade.academy/) library.

## How to play
You can play the game by downloading the stand-alone binary version, which can be found in the releases.

Alternatively, you can install all of the dependencies, then run the python script yourself:
```
pip install --user -r requirements.txt && python main.py
```
Using pipenv :
```
pipenv sync && pipenv run python main.py
```

![screenshot](screenshot.png "Screenshot")


## Play with other words

Run the program with the option `--word-list <list-file>.yaml` to use the
custom words in the indicated file, for example

    python main.py --word-list words-en.yaml

This file is a [yaml](https://yaml.org/) file that you can easily edit with a
text editor.

Note for foreign languages: Currently only the basic set of
[Ascii characters](https://en.wikipedia.org/wiki/ASCII)
are supported, i.e. no umlauts, accents etc.
