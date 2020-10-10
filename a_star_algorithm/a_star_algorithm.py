import pygame
import math
from queue import PriorityQueue

# Setting up the window
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path-finding Algorithm Demo")

# Defining values of colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


# Defining the properties of each Node/ Spot
class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    # Check if spot has been considered.
    def is_closed(self):
        return self.colour == RED

    # Check if spot is in open set
    def is_open(self):
        return self.colour == GREEN

    # Check if a spot is a barrier
    def is_barrier(self):
        return self.colour == BLACK

    # Check if a given spot is the start node
    def is_start(self):
        return self.colour == ORANGE

    # Check if a given spot is the end node
    def is_end(self):
        return self.colour == TURQUOISE

    def reset(self):
        self.colour = WHITE

    # Change spot to closed.
    def make_closed(self):
        self.colour = RED

    # Add spot to open set
    def make_open(self):
        self.colour = GREEN

    # Turn a spot into a barrier
    def make_barrier(self):
        self.colour = BLACK

    # Change a node into a start node
    def make_start(self):
        self.colour = ORANGE

    # Change a given node into a end node
    def make_end(self):
        self.colour = TURQUOISE

    # Make a path
    def make_path(self):
        self.colour = PURPLE

    # Draw rectangles
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    # Update neighbours
    def update_neighbours(self):
        pass

    # Compare spots using less than function

    def __lt__(self, other):
        return False


# Heuristic Function. P1 and P2 are points on the graph (coordinates) i.e P1 = (a, b). It is used to calculate the
# Manhattan distance between two points
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Making the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


# Drawing the grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY, (j * gap, 0), (j * gap, width))


# Draw function to create the grid
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


# Function to change colour using mouse-click
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pass
    pygame.quit()


main(WIN, WIDTH)
