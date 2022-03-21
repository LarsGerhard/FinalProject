# Setup
from numpy import linspace, zeros
from ParticleMagField import magFieldSolve
from scipy.constants import e, m_p
import pygame

# Set recommended initial parameters
qu = 1  # Charge of the particle (Unitless)

mu = 1  # Mass of the particle (Unitless)

B0u = 1  # Magnetic Field Strength (10e-4 Teslas)

v0u = 3  # Initial x Velocity (10^4 Metres / Second)

# Convert initial parameters
B0 = B0u * 10 ** -4  # Magnetic Field Strength (Teslas)

q0 = qu * e  # Converts charge to be units of fundamental charge

m0 = mu * m_p  # Converts mass to be units of proton mass

# Set time interval
tupper = 1e-3  # Upper bound of time (Seconds)

tspace = 1000  # Number of data points to be collected in time interval

t = linspace(0, tupper, tspace)  # Array of time data points

dt = tupper / tspace  # Time between each data point (Seconds)

# Pygame setup
pygame.init()

# Create window dimentions

winLength = 720

# Create window
win = pygame.display.set_mode((winLength, winLength))

# Set Window name
pygame.display.set_caption("Charged Particle in a Magnetic Field")

# Marks that the program and experiment should run, and sets necessary booleans
run = True

runexp = False

rerun = False

addq = False

removeq = False

addB = False

removeB = False

addv = False

removev = False

addm = False

removem = False

# Load some colours

black = (0, 0, 0)

white = (255, 255, 255)

# Button Clicked
buttonp = (170, 170, 170)

# Button Unclicked
buttonup = (100, 100, 100)

# Load fonts
textfont = pygame.font.SysFont('Corbel', 25)

titlefont = pygame.font.SysFont('Corbel', 70)

subtitlefont = pygame.font.SysFont('Corbel', 35)

# Load used text
titleText = titlefont.render('    Magnetic Field Simulation', True, black)

tutorialText1 = subtitlefont.render(
    'Press buttons to adjust the initial parameters, or press Run', True, black)

tutorialText2 = subtitlefont.render(
    'Experiment to see what happens!', True, black)

exitText = subtitlefont.render('Exit', True, black)

rerunText = subtitlefont.render('Rerun', True, black)

continueText = subtitlefont.render('    Back', True, black)

runText = subtitlefont.render('Run Experiment', True, black)

chargetext = textfont.render('Charge', True, black)

addqtext = subtitlefont.render(' +q', True, black)

removeqtext = subtitlefont.render('  -q', True, black)

Btext = textfont.render('Magnetic Field', True, black)

addBtext = subtitlefont.render(' +B', True, black)

removeBtext = subtitlefont.render('  -B', True, black)

vtext = textfont.render('Velocity', True, black)

addvtext = subtitlefont.render(' +v', True, black)

removevtext = subtitlefont.render('  -v', True, black)

mtext = textfont.render('Mass', True, black)

addmtext = subtitlefont.render(' +m', True, black)

removemtext = subtitlefont.render('  -m', True, black)

# Function for creating multiple buttons easily
def Button(pos, w, h, text):
    buttonPressed = False
    # Checks if the button is currently being pressed
    if pygame.mouse.get_pressed()[0]:
        if pos[0] - w / 2 <= mouse[0] <= pos[0] + w / 2 and pos[1] - h / 2 <= mouse[1] <= pos[1] + h / 2:
            buttonPressed = True

    # Renders Button
    if pos[0] - w / 2 <= mouse[0] <= pos[0] + w / 2 and pos[1] - h / 2 <= mouse[1] <= pos[1] + h / 2:
        pygame.draw.rect(win, buttonp, [pos[0] - w / 2, pos[1] - h / 2, w, h])


    else:
        pygame.draw.rect(win, buttonup, [pos[0] - w / 2, pos[1] - h / 2, w, h])

    # Adding text to button
    win.blit(text, (pos[0] - w / 4, pos[1] - h / 4))

    return buttonPressed


# Basic program loop
while run:
    # Basic program loop setup
    # Sets time delay (in ms)
    pygame.time.delay(5)

    # Gets mouse coordinates
    mouse = pygame.mouse.get_pos()

    # Button click logic

    # Creates blank screen
    win.fill((255, 255, 255))

    # Sets title
    win.blit(titleText, (0, 0))

    # Sets description
    win.blit(tutorialText1, (0, 50))
    win.blit(tutorialText2, (0, 80))

    # Button to check if user wants to run the experiment
    if not runexp:
        runexp = Button((winLength / 2, 630), 300, 75, runText)

    # Checks if the user wants to quit
    run = not Button((winLength - 50, winLength - 25), 100, 50, exitText)

    # Displays the current charge
    chargeCount = subtitlefont.render("The particle's charge is: " + str(qu) + " (Units: e)", True, black)

    win.blit(chargeCount, (100, 400))

    # Creates charge button charge description:
    win.blit(chargetext, (50, 175))

    # Creates button to add charge
    if qu < 5 and not addq:
        addq = Button((100, 250), 100, 50, addqtext)

    if addq and pygame.mouse.get_pressed()[0] == False:
        qu += 1
        addq = False

    # Creates button to remove charge
    if qu > -5 and not removeq:
        removeq = Button((100, 325), 100, 50, removeqtext)

    if removeq and pygame.mouse.get_pressed()[0] == False:
        qu -= 1
        removeq = False

    # Displays the current B Field
    BCount = subtitlefont.render("The magnetic field strength is: " + str(B0u) + " (Units: 10^-4 T)", True, black)

    win.blit(BCount, (100, 450))

    # Creates B field button charge description:
    win.blit(Btext, (150, 175))

    # Creates button to add B field strength
    if B0u < 5 and not addB:
        addB = Button((250, 250), 100, 50, addBtext)

    if addB and pygame.mouse.get_pressed()[0] == False:
        B0u += 1
        addB = False

    # Creates button to remove B Field Strength
    if B0u > -5 and not removeB:
        removeB = Button((250, 325), 100, 50, removeBtext)

    if removeB and pygame.mouse.get_pressed()[0] == False:
        B0u -= 1
        removeB = False

    # Displays the current velocity
    velocityCount = subtitlefont.render("The particle's initial velocity is: " + str(v0u) + " (Units: 10^4 m/s)", True, black)

    win.blit(velocityCount, (100, 500))

    # Creates charge button charge description:
    win.blit(vtext, (350, 175))

    # Creates button to add velocity
    if v0u < 5 and not addv:
        addv = Button((400, 250), 100, 50, addvtext)

    if addv and pygame.mouse.get_pressed()[0] == False:
        v0u += 0.5
        addv = False

    # Creates button to remove velocity
    if v0u > 0 and not removev:
        removev = Button((400, 325), 100, 50, removevtext)

    if removev and pygame.mouse.get_pressed()[0] == False:
        v0u -= 0.5
        removev = False

    # Displays the current mass
    mCount = subtitlefont.render("The particle's mass is: " + str(mu) + " (Units: AU)", True, black)

    win.blit(mCount, (100, 550))

    # Creates charge button mass description:
    win.blit(mtext, (500, 175))

    # Creates button to add mass
    if mu < 5 and not addm:
        addm = Button((550, 250), 100, 50, addmtext)

    if addm and pygame.mouse.get_pressed()[0] == False:
        mu += 1
        addm = False

    # Creates button to remove mass
    if mu > 1 and not removem:
        removem = Button((550, 325), 100, 50, removemtext)

    if removem and pygame.mouse.get_pressed()[0] == False:
        mu -= 1
        removem = False

    # Checks if user hits close in window
    for event in pygame.event.get():
        # Checks if corner close button is pressed
        if event.type == pygame.QUIT:
            run = False

    # Runs Experiment if runexp is true
    if runexp:

        rerun = False

        # Convert initial parameters
        B0 = B0u * 10 ** -4  # Magnetic Field Strength (Teslas)

        q0 = qu * e  # Converts charge to be units of fundamental charge

        m0 = mu * m_p  # Converts mass to be units of proton mass

        # Pack parameters

        Pin = (m0, q0, B0)

        # Set recommended and necessary initial conditions
        x0 = 100  # Initial x position (1 / 40 metres)
        y0 = 360  # Initial y position (1 / 40 metres)
        dx0 = v0u * 10 ** 4  # Initial x velocity (metres / second)
        dy0 = 0  # Initial y velocity (metres / second)

        # Pack initial conditions
        Vin = [x0, dx0, y0, dy0]

        # Predetermines path of particle and loads coordinates

        xout, yout, xvout, yvout = magFieldSolve(t, Vin, Pin)

        x = x0
        y = y0

        # Create empty trajectory array

        trax = zeros(int(len(xout)))

        tray = zeros(int(len(yout)))

        tracount = 0

        # Determine how long the B field is off for at the beginning and end
        tintro = 200

        # Determines colour of particle based on charge
        if q0 < 0:
            c = (0, 25, 100 + 25 * abs(qu))
        elif q0 > 0:
            c = (100 + 25 * qu, 25, 0)
        else:
            c = (0, 50, 0)

        # Determines if magnetic field background should be into or out of page

        if B0 > 0:
            bg = pygame.image.load("dots.png").convert()

        else:
            bg = pygame.image.load("Crosses.jpg").convert()

        # Runs over each point in time
        # Run introduction
        i = 0

        while runexp:

            # Sets delay inbetween time intervals (To allow user to see particle motion)
            pygame.time.delay(5)

            # Creates blank screen
            win.fill((255, 255, 255))

            # Introduction Motion
            if i < tintro:

                x += xvout[0] * 40 * dt
                y += yvout[0] * 40 * dt

            # Plots B field motion
            elif i < len(t) + tintro:

                # Changes coordinates of particle based on calculated velocity

                x += float(xvout[i - tintro]) * 40 * dt

                y += float(yvout[i - tintro]) * 40 * dt

                # If there is a magnetic field, loads image of field

                if B0 != 0:
                    win.blit(bg, (0, 0))

            # Ending Motion
            elif i < len(t) + tintro * 3 - 1:
                x += xvout[len(t) - 1] * 40 * dt
                y += yvout[len(t) - 1] * 40 * dt

            else:
                mouse = pygame.mouse.get_pos()

                rerun = Button((winLength - 720 + 75, winLength - 25), 150, 50, rerunText)

                runexp = not Button((winLength - 720 / 2, winLength - 25), 250, 50, continueText)

                run = not Button((winLength - 50, winLength - 25), 100, 50, exitText)

            # Draws trajectory path
            if i % 10 == 1:
                trax[tracount] = x
                tray[tracount] = y
                if tracount < 200:
                    tracount += 1

            for j in range(tracount):
                pygame.draw.circle(win, (0, 255, 255), (float(trax[j]), float(tray[j])), 5)

            # Draws outline at coordinates
            pygame.draw.circle(win, (0, 0, 0), (float(x), float(y)), 10 * mu + 3)

            # Draws particle at coordinates
            pygame.draw.circle(win, c, (float(x), float(y)), 10 * mu)

            # Exit and Experiment Run Condition Checks
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
            if not runexp:
                pygame.time.delay(100)
                break
            if rerun:
                pygame.time.delay(100)
                break
            if not run:
                pygame.time.delay(100)
                break

            # Updates screen with all drawn objects, in order
            pygame.display.update()
            i += 1
    # Updates screen with all drawn objects, in order

    pygame.display.update()
# Closes window
pygame.quit()
