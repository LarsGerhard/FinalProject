# Setup
from numpy import linspace
import pygame
from ParticleMagField import magFieldSolve
from scipy.constants import e, m_p

# Set parameters

B0 = 1e-4  # In Teslas, out of the page

qu = 2  # Charge of the particle (in elementary charge)

mu = 2  # Mass of the particle (In proton masses)

q0 = qu * e  # Converts charge to be units of fundamental charge

m0 = mu * m_p  # Converts mass to be units of proton mass

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

# Indicates pygame is running
run = True

# Predetermine path of particle

xout, yout, xvout, yvout = magFieldSolve(t, Vin, Pin)

x = x0
y = y0

# Determines colour of particle
if q0 < 0:
    c = (0, 25, 100 + 40 * abs(qu))
elif q0 > 0:
    c = (100 + 40 * qu, 25, 0)
else:
    c = (0, 50, 0)

hasrun = False

if B0 > 0:
    bg = pygame.image.load("dots.png")

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

    win.fill((255, 255, 255))

    # drawing particle on screen

    if not hasrun:
        for i in range(len(t)):

            pygame.time.delay(1)

            win.fill((255, 255, 255))

            if B0 != 0:
                win.blit(bg, (-30, -30))

            x += float(xvout[i]) * 40 * dt

            y += float(yvout[i]) * 40 * dt

            pygame.draw.circle(win, (0, 0, 0), (float(x), float(y)), 10 * mu + 3)

            pygame.draw.circle(win, c, (float(x), float(y)), 10 * mu)

            pygame.display.update()

            # Exit and Hasrun Condition Checks

            for event in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT:
                    # it will make exit the while loop
                    run = False

            if i >= len(t) - 1:
                hasrun = True
                break

            if not run:
                break

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
