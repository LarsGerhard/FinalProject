# Setup
from numpy import linspace
import pygame
from ParticleMagField import magFieldSolve
from scipy.constants import e, m_p

# Set parameters

B0 = 1e-4  # In Teslas, out of the page

n1 = 1  # Charge of the particle (in elementary charge)

n2 = 1  # Mass of the particle (In proton masses)

q0 = n1 * e  # Converts charge to be units of fundamental charge

m0 = n2 * m_p # Converts mass to be units of proton mass


tupper = 1e-3

tspace = 1000

t = linspace(0, tupper, tspace)

dt = tupper / tspace

# Pack parameters

Pin = (m0, q0, B0)

# Set initial conditions

x0 = 360
y0 = 360
dx0 = 3.4e4
dy0 = 0

# Pack initial conditions

Vin = [x0, dx0, y0, dy0]

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((720, 720))

# set the pygame window name
pygame.display.set_caption("Charged Particle in a Moving Magnetic Field (Simulation)")

# dimensions of the object
width = 20
height = 20

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# Predetermine path of particle

xout, yout, xvout, yvout = magFieldSolve(t, Vin, Pin)

x = x0
y = y0

hasrun = False

if B0 > 0:
    bg = pygame.image.load("dots.webp")

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False

    win.fill((255,255,255))



    # drawing particle on screen

    for i in range(len(t)):
        pygame.time.delay(10)

        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # it will make exit the while loop
                run = False
                break

        win.fill((255, 255, 255))

        win.blit(bg, (-30, -30))

        x += float(xvout[i]) * 40 * dt

        y += float(yvout[i]) * 40 * dt

        pygame.draw.circle(win, (0, 255, 60), (float(x), float(y)), 10 * n2)
        pygame.display.update()
        if i == len(t) - 1:
            run = False

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
