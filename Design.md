# DESIGN.md

Cavern Master was refactored to introduce clearer separation of responsibilities while preserving the original gameplay logic. The primary architectural changes were:

* A **screen-based architecture** to manage game states
* A **separate input system** to manage inputs separate from the game
* A **pause system** implemented at the screen level

Other code was functionally unchanged.


## Screen Architecture

Each Screen represents a different game state where the `App` owns the currently active screen and each screen has its own update and draw function. Each screen is switched by using  app.change_screen(new_screen) which circumvents the global state switch and makes the transitions more apparent.


## Input Handling
Instead of reading directly from the keyboard as in the original logic it was replaced by an inputstate class. The new input manager polls the keyboard state and performs edge detection



## Pause System


The Pause Screen which is a new addition  is handled by `PlayScreen`; it works by pressing the pause key which toggles the paused state.During the pause the `Game` is not updated and so the game state is frozen and a pause overlay is rendered on top.
