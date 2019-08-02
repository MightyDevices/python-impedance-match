import numpy as np

# frequency of operation (in Hz)
F = 2.45e9

# return loss without series resistor (in dB)
RL = 4.80
# return loss with the series resistor (in dB)
RL_R = 5.23

# system impedance (in Ohms)
RS = 50.0
# series resistance (in Ohms)
RR = 30.0


# get gamma magnitude for given return loss
def get_gamma(rl):
    return 10**(-rl/20)


# get the 'little gamma' factor
def get_little_gamma(rs, gamma):
    return rs * (gamma**2 + 1) / (gamma**2 - 1)


# get 'a' value
def get_a(gamma, gamma_r, rs, rr):
    # get little gammas
    lg = get_little_gamma(rs, gamma)
    lgr = get_little_gamma(rs, gamma_r)
    # get the result
    return 0.5 * (rr**2 + 2 * rr * lgr) / (lg - lgr - rr)


# get one of the 'b' values (positive one is returned)
def get_b(a, gamma, rs):
    # get little gamma
    lg = get_little_gamma(rs, gamma)
    # get the result
    return np.sqrt(-(a**2 + 2 * a * lg + rs**2))


# return the inductance value for given impedance (b) at given frequency (f)
def get_L(b, f):
    return b / (2 * np.pi * f)


# return the capacitance value for given impedance (b) at given frequency (f)
def get_C(b, f):
    return 1 / (2 * np.pi * f * b)


# gamma magnitude without series resistor
GAMMA = get_gamma(RL)
# gamma magnitude with series resistor
GAMMA_R = get_gamma(RL_R)

# compute both parameters
a = get_a(GAMMA, GAMMA_R, RS, RR)
b = get_b(a, GAMMA, RS)

# show the results
print(f"impedance = {a} +/- j{b}")
print(f"inductor value = {get_L(b, F)}, capacitor value = {get_C(b, F)}")
