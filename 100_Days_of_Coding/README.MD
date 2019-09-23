# 100 Days of Coding! 
- Started 9/3/19
- From Python basics, pygame simulation, some web development, machine learning, and data science
## Data Science Project: Video Game Classification [ACTIVE](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/blob/master/Machine_Learning_Projects/testing.ipynb)
Day 12 
 - Implemented Linear Regression and Decision Trees
Day 11
 - Data Wrangling and cleaning
Day 10
- Started juypter notebook and uploaded dataset

## Django Web Development [ON HOLD Currently]

[Day 10](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Web_Applications)
- Made Home page

[Day 9.5](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Web_Applications)
- Began making a sample web app using Django


## Aliens Invasion Simulation game based on pygame library
Difficulty - ***

[Day 9](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Video%20Game%20Project) 
- Refactored some of the code
- Later looking to have the aliens be able to fire bullets 

[Day 8](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Video%20Game%20Project) 
- 9/11
- Finshing last elements for the game 
  - Displaying the current level, highscore, and number of ships the player has left

[Day 7](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Video%20Game%20Project) 
- 9/10
- Made a button for the player to start the game, so the player isnt playing as soon as we run the code
- Integrated a scoreboard and a limited number of attempts or lives
- Refactored settings and Added criteria for speeding up the game
- Button Class, Scoreboard Class


[Day 5 - 6](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/Python_Crash_Course_Coding_Tutorial/Video%20Game%20Project) 
- 9/8 - 9/9
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


## Python Basics:

[Day Four](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day_4)
- 9/7
- Unit testing functions and classes
- Difficulty ***

[DAY THREE](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day_3)
- 9/6
- Random variables, Reading and Writing, Exceptions
- Difficulty *

[DAY TWO](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day%202)
- 9/4
- Dictionaries,User Input Funtions, Classes 
- Difficulty *

Contains simple python excercises for the purposes for refreshing from the book: Python Crash Course by Eric Matthes
[DAY ONE](https://github.com/marctheshark3/Leopard-Shark-Code-Repo/tree/master/100_Days_of_Coding/Day%201)
- 9/3
- Intro, Variables, Data Types, Dictionaries
- Difficulty *
