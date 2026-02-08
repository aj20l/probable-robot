from screens.menu import MenuScreen

class App:
    def __init__(self):
        self.screen = MenuScreen(self)  
    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self, input_state):
        self.screen.update(input_state)

    def draw(self, screen):
        self.screen.draw(screen)  

class Screen:
    def __init__(self, app):
        self.app = app

    def update(self):
        pass

    def draw(self):
        pass
                
