# input.py
from dataclasses import dataclass
from pgzero.keyboard import keyboard


@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool   


class InputManager:
    def __init__(self):
        self._prev_space = False
        self._prev_p = False

    def poll(self) -> InputState:
        #reads (level)
        left = keyboard.left
        right = keyboard.right
        space = keyboard.space
        up = keyboard.up
        p = keyboard.p

        #  edge detection 
        fire_pressed = space and not self._prev_space
        jump_pressed = fire_pressed
        pause_pressed = p and not self._prev_p

        # remember for next frame
        self._prev_space = space
        self._prev_p = p

        return InputState(
            left=left,
            right=right,
            jump_pressed=up,
            fire_pressed=fire_pressed,
            fire_held=space,
            pause_pressed=pause_pressed,
        )
