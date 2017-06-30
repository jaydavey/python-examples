#!/usr/bin/python

# Example code for reading a gaming controller with joysticks via pygame
# Jay's first Pygame program

VERSION = "0.4"

#Intialize pygame.  https://www.pygame.org/docs/tut/ImportInit.html
try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print("\nImportError. Couldnt load module.")
    sys.exit(2)

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Jay\'s first Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("-\_(:P)_/-", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit (render) everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # [create new object as instance of ball class]
    ball = Ball()

    # Event loop
    while 1:
        # [check for user input]
        for event in pygame.event.get():
            if event.type == QUIT:
                return
	    elif event.type == KEYDOWN:
	        if event.key == K_UP:
	            player.moveup()
	        if event.key == K_DOWN:
	            player.movedown()
	    elif event.type == KEYUP:
	        if event.key == K_UP or event.key == K_DOWN:
	            player.movepos = [0,0]
	            player.state = "still"

        # [call ball's update function]
        ball.update()

        # [check for collisions]
		if not self.area.contains(newpos):
			tl = not self.area.collidepoint(newpos.topleft)
			tr = not self.area.collidepoint(newpos.topright)
			bl = not self.area.collidepoint(newpos.bottomleft)
			br = not self.area.collidepoint(newpos.bottomright)
			if tr and tl or (br and bl):
			      angle = -angle
			if tl and bl:
			      self.offcourt(player=2)
			if tr and br:
			      self.offcourt(player=1)
		else:
		    # Deflate the rectangles so you can't catch a ball behind the bat
		    player1.rect.inflate(-3, -3)
		    player2.rect.inflate(-3, -3)

		    # Do ball and bat collide?
		    # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
		    # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
		    # bat, the ball reverses, and is still inside the bat, so bounces around inside.
		    # This way, the ball can always escape and bounce away cleanly
		    if self.rect.colliderect(player1.rect) == 1 and not self.hit:
		        angle = math.pi - angle
		        self.hit = not self.hit
		    elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
		        angle = math.pi - angle
		        self.hit = not self.hit
		    elif self.hit:
		        self.hit = not self.hit
		self.vector = (angle,z)

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
