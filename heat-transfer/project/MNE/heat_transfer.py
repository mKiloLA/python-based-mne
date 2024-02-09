from math import pi

class PropertyNotImplemented(Exception):
    pass


# These equations were created using scipy.optimize.curve_fit and a fourth order polynomial.
def water_properties(x, prop):
    if prop == 'Pressure':
        a,b,c,d,e = 1.16967270e-08, -1.35623438e-05,  5.94563626e-03, -1.16661469e+00, 8.63515668e+01
    elif prop == 'Specific Volume':
        a,b,c,d,e = 9.36189536e-14, -1.32157097e-10,  7.29410417e-08, -1.79074230e-05, 2.62088397e-03
    elif prop == 'Heat of Vaporization':
        a,b,c,d,e = 2.45826897e-08, -4.62307908e-05,  2.79341628e-02, -9.29361160e+00, 3.76075206e+03
    elif prop == 'Specific Heat':
        a,b,c,d,e = 9.97282023e-07, -1.39283158e-03,  7.35844689e-01, -1.73497370e+02, 1.95310023e+04
    elif prop == 'Viscosity':
        a,b,c,d,e = 1.22370934e-11, -1.78198097e-08,  9.75386832e-06, -2.38221442e-03, 2.19688033e-01
    elif prop == 'Thermal Conductivity':
        a,b,c,d,e = 2.27856649e-10, -3.01583421e-07,  1.41813193e-04, -2.68099167e-02, 2.19025428e+00
    elif prop == 'Prandtll Number':
        a,b,c,d,e = 1.03046179e-07, -1.50022081e-04,  8.20422942e-02, -1.99992466e+01, 1.83775100e+03
    elif prop == 'Oil Specific Heat':
        a,b,c,d,e = 7.57640461e-07, -1.16948468e-03,  6.76308996e-01, -1.69259798e+02, 1.72835141e+04
    else:
        raise PropertyNotImplemented("Property not implemented for water.")
    return (a*x**4+b*x**3+c*x**2+d*x+e)

def oil_properties(x, prop):
    if prop == 'Specific Heat':
        a,b,c,d,e = 7.57640461e-07, -1.16948468e-03,  6.76308996e-01, -1.69259798e+02, 1.72835141e+04
    else:
        raise PropertyNotImplemented("Property not implemented for oil.")
    return (a*x**4+b*x**3+c*x**2+d*x+e)

def reynolds_num(flow_rate, diameter, viscosity, tubes=1):
    return ((4*flow_rate) / (tubes*pi*diameter*viscosity))