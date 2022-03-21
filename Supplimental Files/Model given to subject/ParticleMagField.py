from scipy.integrate import odeint

# Differential Equation

def ratefunc(t, V, m, q, B):
    # Determines the rate of change for position in both the x and y directions
    # Unpack initial conditions
    x, u, y, v = V

    f = [u, ((q * B) / m) * v, v, (-(q * B) / m) * u]

    return f

# Solver

def magFieldSolve(t, Vin, Pin):

    sol = odeint(ratefunc, Vin, t, args=Pin, tfirst= True)

    # Unpack positions and velocities

    xout = sol[:,[0]]
    xvout = sol[:,[1]]
    yout = sol[:,[2]]
    yvout = sol[:,[3]]

    return xout, yout, xvout, yvout




