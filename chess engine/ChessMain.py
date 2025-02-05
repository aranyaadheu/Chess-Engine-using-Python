"""
This is our main driver file. It will be responsible for handeling user input and displaying the current GameState object.

"""
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 is another option.
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later on. 
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main.
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
     # for loop to make this code more efficient and it saves time. 
     #Note: we can acces an image by saying 'IMAGES['wp']'

'''
The main driver for our code. This will handle user input and update the graphics. 

'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState() # gs = gamestate
    print(gs.board)
    loadImages() #only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state. 

'''

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board. 
    #add in piece of ihghlighting or move suggestions (later)
    drawPieces(screen, gs.board) #draw pieces on top of those squares.


'''
Draw the squares on the board. 

'''

def drawBoard(screen):



'''
draw the pieces on the board using the current GameState.board

'''

def drawPieces(screen, board):

if __name__ == "__main__":
    main()

