# Setup
from numpy import linspace
import pygame
from ParticleMagField import magFieldSolve
from scipy.constants import e, m_p

# Set initial parameters


qu = 3  # Charge of the particle (Unitless)

mu = 1  # Mass of the particle (Unitless)

B0u = 1 # Magnetic Field Strength (10e-4 Teslas)

v0u = 3 # Initial x Velocity (10^4 Metres / Second)

B0 = B0u * 10**-4  # Magnetic Field Strength (Teslas)

q0 = qu * e  # Converts charge to be units of fundamental charge

m0 = mu * m_p  # Converts mass to be units of proton mass

tupper = 1e-3  # Upper bound of time (Seconds)

tspace = 1000  # Number of data points to be collected in time interval

t = linspace(0, tupper, tspace)  # Array of time data points

dt = tupper / tspace  # Time between each data point (Seconds)

# Pack parameters

Pin = (m0, q0, B0)

# Set initial conditions

x0 = 360  # Initial x position (1 / 40 metres)
y0 = 360  # Initial y position (1 / 40 metres)
dx0 = v0u * 10**4  # Initial x velocity (metres / second)
dy0 = 0  # Initial y velocity (metres / second)

# Pack initial conditions

Vin = [x0, dx0, y0, dy0]

# Activate Pygame
pygame.init()

# Create window
win = pygame.display.set_mode((720, 720))

# Set Window name
pygame.display.set_caption("Charged Particle in a Moving Magnetic Field (Simulation)")

# Marks that the program and experiment should run
run = True

runexp = True

# Predetermines path of particle

xout, yout, xvout, yvout = magFieldSolve(t, Vin, Pin)

x = x0
y = y0

# Determines colour of particle based on charge
if q0 < 0:
    c = (0, 25, 100 + 40 * abs(qu))
elif q0 > 0:
    c = (100 + 40 * qu, 25, 0)
else:
    c = (0, 50, 0)

# Determines if magnetic field background should be into or out of page

if B0 > 0:
    bg = pygame.image.load("dots.png")

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # Checks if user wants to close program, sets run to false if they do
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    # Creates blank screen

    win.fill((255, 255, 255))

    # Runs Experiment if runexp is true

    if runexp:

        # Runs over each point in time

        for i in range(len(t)):

            # Sets delay inbetween time intervals (To allow user to see particle motion)

            pygame.time.delay(1)

            # Creates blank screen

            win.fill((255, 255, 255))

            # If there is a magnetic field, loads image of field

            if B0 != 0:
                win.blit(bg, (0, 0))

            # Changes coordinates of particle based on calculated velocity

            x += float(xvout[i]) * 40 * dt

            y += float(yvout[i]) * 40 * dt

            # Draws outline at coordinates

            pygame.draw.circle(win, (0, 0, 0), (float(x), float(y)), 10 * mu + 3)

            # Draws particle at coordinates

            pygame.draw.circle(win, c, (float(x), float(y)), 10 * mu)

            # Updates screen with all drawn objects, in order

            pygame.display.update()

            # Exit and Experiment Run Condition Checks

            for event in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT:
                    # it will make exit the while loop
                    run = False

            if i == len(t) - 1:
                runexp = False

            if not run:
                break

    # Updates screen with all drawn objects, in order
    pygame.display.update()

# Closes window
pygame.quit()
