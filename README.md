# Cavern Refactor
This game can be run by:
Opening the command line in a python enabled environment and entering
` python .\main.py` 

Outside of minor cleanup required by refactoring, the original game logic was mostly unaffected. The code was modularised by introducing separate screens for each game state and by using a separate input manager to handle player actions instead of reading directly from the keyboard.
