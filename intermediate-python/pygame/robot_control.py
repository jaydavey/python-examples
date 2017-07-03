"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Show everything we can pull off the joystick
"""
import pygame
import sys
sys.path += ['/home/jay/python/python-examples/dev/StateMachine', '/home/jay/python/transitions']
from transitions import Machine
import random
from robotFSM import MobileNest
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
 # Define controller button mapping
controller_btn = {"A":0, "B":1, "X":2, "Y":3, "LB":4, "RB":5, "BACK":6, "START":7, "MODE":8, "LTHUMB":9, "RTHUMB":10} 
 
class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 20)
 
    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height
 
    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15
 
    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10
 
    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10
 
 
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Jays robot controller")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
 
# Get ready to print
textPrint = TextPrint()

#------Finite State Machine setup-------
nest123 = MobileNest("Nest123")
 
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released")

        # STATE MACHINE CONTROL STEP
        CURRENT_STATE = nest123.state
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        if CURRENT_STATE == 'charging':
            #check if we're fully charged yet.
            if joystick.get_button(controller_btn["X"]) == 1:
                nest123.fully_charged()

        elif CURRENT_STATE == 'waiting_for_trajectory':
            #do the wait for nav thing
            if joystick.get_button(controller_btn["B"]) == 1:
                nest123.received_trajectory()

        elif CURRENT_STATE == 'navigating_trajectory':
            #do the nav thing
            if joystick.get_button(controller_btn["RB"]) == 1:
                nest123.reached_charging_station()
            elif joystick.get_button(controller_btn["A"]) == 1:
                nest123.reached_end_of_trajectory()

        elif CURRENT_STATE == 'scheduling_re-charge_stop':
            #do the reschedule thing
            if joystick.get_button(controller_btn["LB"]) == 1:
                nest123.recharge_scheduled()


    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()
 
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
 
    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()
 
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
 
        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()
 
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))
 
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()
 
        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()
 
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()
 
        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()
 
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()
 
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()
 
        textPrint.unindent()

        # Print all state machine values and variables here
        textPrint.print(screen, "")
        textPrint.print(screen, "Current State: {}".format(nest123.state))

 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
