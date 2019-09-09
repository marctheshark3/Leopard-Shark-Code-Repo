# 100 Days of Coding! 
- Started 9/3/19
- From Python basics, some web development, Machine Learning to Data Science

#### Python Basics:
Contains simple python excercises for the purposes for refreshing from the book: Python Crash Course by Eric Matthes
[DAY ONE](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day%201)
- 9/3
- Intro, Variables, Data Types, Dictionaries
- Difficulty *

[DAY TWO](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day%202)
- 9/4
- Dictionaries,User Input Funtions, Classes 
- Difficulty *

[DAY THREE](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day_3)
- 9/6
- Random variables, Reading and Writing, Exceptions
- Difficulty *

[Day Four](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day_4)
- 9/7
- Unit testing functions and classes
- Difficulty ***

[Day 5 - 6](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Video%20Game%20Project) 
- 9/8 - 9/9
- Aliens Invasion Simulation game based on pygame library
- Functionality:
  - Bitmap file loaded for ship
  - Able to move ship via arrow keys
  - Fire bullets and remove the disappearing bullets off screen
  - Various Classes:
    - Alien Invasion: Holds main functionality of the game and interal functions
    - Setting: Holds all of the settings like game window size, ships speed, to number of bullets in one convient spot
    - Ship: Holds the functionality for the ship that the user controls 
    - Bullet: Holds the functionality for the bullets the user fires
   - Run_game function Snip:
```python
def run_game(self):
        ''' Start the main loop for the game'''

        while True:
        
            #internal function for checking for keyboard inputs
            self._check_events()
            
            if self.stats.game_active:
            
              #updates the ships position if there were any previous keyboard inputs
              self.ship.update()
            
              #internal function for updating the bullets position and if they are off screen remove them
              self._update_bullets()
              
              #internal function for update the aliens positing and logic
              self._update_aliens()
            
            #update the screen with the previous updates
            self._update_screen()
```
- Difficulty ***
