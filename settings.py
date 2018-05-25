
# Sets window's title:
windowTitle = "Foxy"

# Screen settings:
screen_width, screen_height = 1280, 640
screen_size = (screen_width, screen_height)

# Setting up FPS:
framesPerSecond = 45

# Variables:
done = None
playerHit = None
winner = None
playerTurn = "1"

# Colors:
black = (0, 0, 0)
red = (182, 38, 37)
white = (255, 255, 255)
gray = (64, 64, 64)

# Main Screen:
main_text = ("Welcome to Foxy!",
             "Press Enter to Play.")

# Winner Text:
winner_text = ("The Winner Is: {0}!!",
               "Congrats on Winning the Game!",
               "Please Press Enter and Restart the Game")

# Screen_type sets which screen we are using:
# Screen type = "Main Menu"
# Screen type = "Player 1 Name"
# Screen type = "Player 2 Name"
# Screen type = "Playing"
# Screen type = "Game End"
screen_type = "Main Menu"
